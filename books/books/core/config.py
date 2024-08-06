from functools import lru_cache

import redis
from environs import Env
from pydantic_settings import BaseSettings

_env = None


class Settings(BaseSettings):
    async_db_url: str
    db_url: str
    origin: str
    debug: bool
    jwt_pub_key: str
    service_key: str
    bcr_url: str
    detail_url: str
    redis_url: str

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings():
    _settings = Settings()
    return _settings


config = get_settings()


def get_env():
    global _env
    if not _env:
        _env = Env()
        _env.read_env()
    return _env
