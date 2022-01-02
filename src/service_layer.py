import asyncio
from functools import partial

from src.easter_ru import get_xls


async def create_calendar(year: int, start_kathisma: int) -> None:
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, partial(get_xls, year, start_kathisma))
