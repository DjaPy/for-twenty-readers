import asyncio
from datetime import date
from functools import partial

from src.easter_ru import get_xls


async def create_calendar(start_date_kathisma: date, start_kathisma: int, year: int) -> None:
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, partial(get_xls, start_date_kathisma, start_kathisma, year))
