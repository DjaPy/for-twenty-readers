from datetime import datetime

from src.easter_ru import get_xls, get_calendar_for_table


def test_get_calendar_for_table():
    start_date = datetime.now().date()
    year = datetime.now().year
    assert get_calendar_for_table(start_date, year)


def test_get_xls():
    start_date = datetime.now().date()
    start_kathisma = 10
    result = get_xls(start_date, start_kathisma)
