import uvicorn

from src.config import config
from src.entrypoints.fastapi_app import app_server

if __name__ == "__main__":
    uvicorn.run(app_server, host=config.host, port=config.port)
