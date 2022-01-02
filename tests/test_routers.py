import json

import aiohttp
import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_calendar(server, client, config):
    async with client.get(
        url=f'http://127.0.0.1:{config.port}/calendar'
    ) as response:
        assert response.status == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_get_calendar(server, client, config):
    data = aiohttp.FormData()
    year = 'year'
    start_kathisma = 'start_kathisma'
    data.add_field(year, 2022)
    data.add_field(start_kathisma, 1)
    async with client.post(
        url=f'http://127.0.0.1:{config.port}/get-calendar',
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        data=data
    ) as response:
        assert response.status == status.HTTP_200_OK
        resp = await response.text()
        for word in [start_kathisma, year]:
            assert word in resp
