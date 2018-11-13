import itertools

from dateutil import easter
from dateutil import utils
from openpyxl import Workbook, worksheet
from datetime import date, timedelta, datetime



def get_easter(year, type_calendar):
    easter_day = easter.esater(year, type_calendar)
    return easter_day


def get_input_date(year=None):
    if not year:
        year = utils.datetime.now().year
    type_calendar = 1
    easter_day = get_easter(year, type_calendar)
    return easter_day


def get_calendar_reader(ws):
    month_name = {
        "B2": "ЯНВ", "C2": "ФЕВ", "D2": "МАРТ", "E2": "АПР",
        "F2": "МАЙ", "G2": "ИЮН", "I2": "ИЮЛ", "H2": "АВГ",
        "J2": "СЕН", "K2": "ОКТ", "L2": "НОЯ", "M2": "ДЕК"
    }
    for cell_name, cell_value in month_name.items:
        ws[cell_name] = cell_value


def get_number_days_in_year(year):
    days_leap_year = 366
    days_normal_year = 365
    defenition_year = ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
    if defenition_year:
        return days_leap_year
    return days_normal_year


def add_in_ws_number_day(number_cell, ws):
    for number in range(1, 32):
        number_cell += 1
        cell_name = 'A{}'.format(number_cell)
        cell_value = number
        ws[cell_name] = cell_value


def get_list_date(start_no_reading, end_no_reading,
                  start_kathisma, number_days_in_year):
    """Gets a list of dates with an interval when you do not need to read.
    """
    zero_loop = {day: kathisma for day, kathisma in enumerate(range(start_kathisma, 21))}
    start_loop_first = number_days_in_year - len(zero_loop)
    end_loop_first = number_days_in_year - start_no_reading.






def create_dict_kathisma(start_kathisma, year, easter_day):
    """ Creates a dictionary to fill the table excel

    Only 20 kafism, so range(0, 21)
    :param start_kathisma:
    :param year:
    :param easter_day:
    :return:
    """
    total_kathisma = [number_kathisma for number_kathisma in range(1, 21)]
    number_days_in_year = get_number_days_in_year(year)
    start_no_reading = easter_day - timedelta(days=3)
    end_no_reading = easter_day + timedelta(days=6)
    first_loop = [number_kathisma for number_kathisma in range(start_kathisma, 21)]



    dict_day_kathisma = {day: kathisma for day, kathisma in zip(number_days_in_year, itertools.cycle(total_kathisma))}
    return dict_day_kathisma


def get_calendar_for_table(year, start_day):
    current_day = date(day=1, month=1, year=year)
    table_year = {}
    current_day_list = []
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


def create_calendar_for_reader(start_day, year, ws):
    cell_step = 1
    calendar_table = get_calendar_for_table(year)
    frame_month = {(index + 1): symbol for index, symbol in enumerate(
            ['B', 'C', 'D', 'E', 'F', 'G', 'I', 'H', 'J', 'K', 'L', 'M']
    )}
    cell_name_index = 2
    for month, days in calendar_table.items():
        cell_month = frame_month[month]
        for day in days:
            cell_name_index += cell_step
            cell_name = "{}{}".format(cell_month, cell_name_index)
            ws[cell_name] = 0


def get_xls():
    wb = Workbook()
    ws = wb
    dest_file = "calendar_reader.xlsx"
    for number in range(1, 21):
        wb.create_sheet("Кафизма {}".format(number))
        ws = wb.active
        get_calendar_reader(ws)
        get_input_date()

    ws.save(filename=dest_file)

