import itertools
from datetime import date, datetime, timedelta
from typing import Dict, List, Optional, Tuple

from dateutil import easter, utils
from dateutil.easter import EASTER_ORTHODOX
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, Side
from openpyxl.worksheet.worksheet import Worksheet

from src.const import OUT_FILE


def get_easter_day(year: Optional[int] = None) -> date:
    if not year:
        year = utils.today().year
    return easter.easter(year, EASTER_ORTHODOX)


def get_header_of_month(ws: Worksheet) -> Worksheet:
    alignment_month = Alignment(
        horizontal='center',
        vertical='center',
    )
    font_month = Font(
        name='Calibri',
        size=16,
        color='00FF8080',
    )
    month_name = {
        "B2": "ЯНВ", "C2": "ФЕВ", "D2": "МАРТ", "E2": "АПР",
        "F2": "МАЙ", "G2": "ИЮН", "H2": "ИЮЛ", "I2": "АВГ",
        "J2": "СЕН", "K2": "ОКТ", "L2": "НОЯ", "M2": "ДЕК"
    }
    for cell_name, cell_value in month_name.items():
        ws[cell_name] = cell_value
        cell = ws[cell_name]
        cell.alignment = alignment_month
        cell.font = font_month

    return ws


def get_number_days_in_year(year: int) -> int:
    days_leap_year = 366
    days_normal_year = 365
    definition_year = ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
    if definition_year:
        return days_leap_year
    return days_normal_year


def get_column_with_number_day(number_cell: int, ws: Worksheet) -> Worksheet:
    alignment_number_day = Alignment(
        horizontal='center',
        vertical='center',
    )
    font_number_day = Font(
        name='Trebuchet MS',
        size=12,
    )
    for number in range(1, 32):
        number_cell += 1
        cell_name_left = 'A{}'.format(number_cell)
        cell_name_right = 'N{}'.format(number_cell)
        cell_value = number
        ws[cell_name_left] = cell_value
        ws[cell_name_right] = cell_value
        right_cell = ws[cell_name_right]
        left_cell = ws[cell_name_left]
        right_cell.alignment = alignment_number_day
        right_cell.font = font_number_day
        left_cell.alignment = alignment_number_day
        left_cell.font = font_number_day

    return ws


def get_list_date(
    start_no_reading: date,
    end_no_reading: date,
    start_kathisma: int,
    number_days_in_year: int,

) -> Dict[int, int]:
    """Gets a list of dates with an interval, when you do not need to read.
    """
    loop_from_total_kathisma = [number for number in range(1, 21)]
    step_kathisma: int = 1
    zero_loop_first = {(day + 1): kathisma for day, kathisma in enumerate(range(start_kathisma, 21))}
    start_loop_first = len(zero_loop_first) + step_kathisma
    end_loop_first = int(start_no_reading.strftime('%j')) - 1
    start_zero_loop_second = int(end_no_reading.strftime('%j')) + 1
    gen_loop_first = [day for day in range(start_loop_first, (end_loop_first + 1))]
    loop_first = {
        day: kathisma for day, kathisma in zip(gen_loop_first, itertools.cycle(loop_from_total_kathisma))
    }
    end_number_kathisma_first_loop = loop_first[end_loop_first]
    start_number_kathisma_zero_loop_second = end_number_kathisma_first_loop + step_kathisma
    zero_loop_second = {
        (start_zero_loop_second + day): kathisma for day, kathisma in
        enumerate(range(start_number_kathisma_zero_loop_second, 21))
    }
    start_loop_second = start_zero_loop_second + len(zero_loop_second)
    gen_loop_second = [day for day in range(start_loop_second, (number_days_in_year + 1))]
    loop_second = {
        day: kathisma for day, kathisma in zip(gen_loop_second, itertools.cycle(loop_from_total_kathisma))
    }
    all_year_loop = {}
    all_year_loop.update(zero_loop_first)
    all_year_loop.update(loop_first)
    all_year_loop.update(zero_loop_second)
    all_year_loop.update(loop_second)

    return all_year_loop


def get_list_date_without_easter(start_day: int, end_no_reading: date, number_days_in_year: int) -> Dict[int, int]:
    start_zero_loop_second = int(end_no_reading.strftime('%j')) + 1
    if start_day < start_zero_loop_second:
        start_day = start_zero_loop_second
    loop_from_total_kathisma = [number for number in range(1, 21)]
    step_kathisma: int = 1
    start_number_kathisma_zero_loop_second = start_day + step_kathisma
    zero_loop_second = {
        (start_day + day): kathisma for day, kathisma in
        enumerate(range(start_number_kathisma_zero_loop_second, 21))
    }
    start_loop_second = start_zero_loop_second + len(zero_loop_second)
    gen_loop_second = [day for day in range(start_loop_second, (number_days_in_year + 1))]
    loop_second = {
        day: kathisma for day, kathisma in zip(gen_loop_second, itertools.cycle(loop_from_total_kathisma))
    }
    all_year_loop = {}
    all_year_loop.update(zero_loop_second)
    all_year_loop.update(loop_second)

    return all_year_loop


def get_boundary_days(easter_day: date) -> Tuple[date, date]:
    start_no_reading = easter_day - timedelta(days=3)
    end_no_reading = easter_day + timedelta(days=6)
    return start_no_reading, end_no_reading


def get_calendar_for_table(start_calendar_date: date, year: int) -> Dict[int, List[int]]:
    current_day = start_calendar_date
    table_year = {}
    current_day_list: List[int] = []
    current_month = 1

    while current_day.year == year:
        if current_day.day == 1:
            table_year[current_month] = current_day_list
            current_day_list = []
        current_month = current_day.month
        current_day_list.append(current_day.day)
        current_day += timedelta(days=1)
    table_year[current_month] = current_day_list
    return table_year


def add_number_kathisma(ws: Worksheet, number: int) -> None:
    alignment_num_kathisma = Alignment(
        horizontal='center',
        vertical='center',
    )
    font_num_kathisma = Font(
        name='Trebuchet MS',
        size=16,
    )
    border_num_kathisma = Border(
        top=Side(border_style='dashed', color='00000000'),
        bottom=Side(border_style='dashed', color='00000000'),
        left=Side(border_style='dashed', color='00000000'),
        right=Side(border_style='dashed', color='00000000'),

    )
    ws['A2'] = number
    cell_kathisma = ws['A2']
    cell_kathisma.alignment = alignment_num_kathisma
    cell_kathisma.font = font_num_kathisma
    cell_kathisma.border = border_num_kathisma


def create_calendar_for_reader(
    ws: Worksheet,
    calendar_table: Dict[int, List[int]],
    all_kathisma: Dict[int, int],
    year: int
) -> None:
    alignment = Alignment(
        horizontal='center',
        vertical='center',
    )
    font = Font(
        name='Trebuchet MS',
        size=14,
    )
    cell_step = 1
    frame_month = {(index + 1): symbol for index, symbol in enumerate(
        ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    )}
    for month, days in calendar_table.items():
        cell_month = frame_month[month]
        cell_name_index = 2
        for day in days:
            cell_name_index += cell_step
            cell_name = "{}{}".format(cell_month, cell_name_index)
            datestr = '{} {} {}'.format(month, day, year)
            date = datetime.strptime(datestr, '%m %d %Y')
            day_now = date.strftime('%j')
            ws[cell_name] = all_kathisma.get(int(day_now), '')
            cell_kathisma = ws[cell_name]
            cell_kathisma.alignment = alignment
            cell_kathisma.font = font


def get_xls(start_date: date, start_kathisma: int, year: Optional[int]) -> str:
    if not year:
        year = start_date.year
    start_day_kathisma = start_date.timetuple().tm_yday
    wb = Workbook()
    calendar_table = get_calendar_for_table(start_date, year)
    easter_day = get_easter_day(year)
    start_no_reading, end_no_reading = get_boundary_days(easter_day)
    number_days_in_year = get_number_days_in_year(year)
    total_kathisma = 21
    for number in range(1, total_kathisma):
        all_kathismas = {}
        ws = wb.create_sheet("Чтец {}".format(number))
        add_number_kathisma(ws, number)
        get_header_of_month(ws)
        number_cell_for_column = number_days_in_year
        get_column_with_number_day(number_cell_for_column, ws)
        if start_no_reading > start_date:
            all_kathismas = get_list_date(
                start_no_reading,
                end_no_reading,
                start_kathisma,
                number_days_in_year,
            )
        else:
            all_kathismas = get_list_date_without_easter(
                start_day_kathisma, end_no_reading, number_days_in_year
            )
        create_calendar_for_reader(ws, calendar_table, all_kathismas, year)
        if start_kathisma > 19:
            start_kathisma = 0
        start_kathisma += 1

    wb.save(filename=OUT_FILE)
    return str(OUT_FILE)
