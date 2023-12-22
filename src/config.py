from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):

    host: str = Field('127.0.0.1', description='Хост сервера')
    port: int = Field(8000, description='Порт сервера')
    service_name: str = ''

    class Config:
        env_file = ".env"


config = Config()
