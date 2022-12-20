import datetime

from fastapi import APIRouter, Form, Request, Response

from src import service_layer
from src.const import TEMPLATE

app_route = APIRouter()


@app_route.post('/get-calendar')
async def get_calendar(
    request: Request,
    start_date_kathisma: datetime.date = Form(...),
    start_kathisma: int = Form(...),
    year: int = Form(...),
) -> Response:
    await service_layer.create_calendar(start_date_kathisma, start_kathisma, year)
    return TEMPLATE.TemplateResponse('calendar.html', context=dict(request=request, year=year, start_date_kathisma=start_date_kathisma, start_kathisma=start_kathisma))


@app_route.get('/calendar')
async def calendar(req: Request) -> Response:
    return TEMPLATE.TemplateResponse('calendar.html', context=dict(request=req))
