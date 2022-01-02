from fastapi import FastAPI

from src.entrypoints.routers import app_route


def get_application() -> FastAPI:
    app = FastAPI(
        title='Twenty reader',
        description='Service for getting a calendar for Psalter readers',
        docs_url='/doc',
    )

    app.include_router(app_route)
    return app


app_server = get_application()
