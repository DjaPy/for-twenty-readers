from datetime import date

from src.easter_ru import create_xls


def create_calendar(start_date_kathisma: date, start_kathisma: int, year: int) -> None:
    create_xls(start_date_kathisma, start_kathisma, year)
