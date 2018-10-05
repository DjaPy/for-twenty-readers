from dateutil import easter
from dateutil import utils
from openpyxl import Workbook, worksheet


def get_easter(year, type_calendar):
    easter_day = easter.esater(year, type_calendar)
    return easter_day


def get_input_date(kathisma, year=None):
    if not year:
        year = utils.datetime.now().year
    type_calendar = 1
    easter_day = get_easter(kathisma, type_calendar)
    return easter_day

def get_calendar_reader():
    month = {
        "B2": "ЯНВ",
        "C2": "ФЕВ",
        "D2": "МАРТ",
        "E2": "АПР",
        "F2": "МАЙ",
        "G2": "ИЮН",
        "I2": "ИЮЛ",
        "H2": "АВГ",
        "J2": "СЕН",
        "K2": "ОКТ",
        "L2": "НОЯ",
        "M2": "ДЕК",
    }
    number_day = [x for x in list(range(0, 30))]
    day = '{}'.format(number_day)

def get_xls():
    wb = Workbook()
    dest_file = "calendar_reader.xlsx"
    ws1 = wb
    ws1.title = "Кафизма 1"

