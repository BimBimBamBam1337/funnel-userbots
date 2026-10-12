from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from src.config import Config, settings


def build_redis(config: Config) -> Redis:
    redis = Redis.from_url(config.redis.url.get_secret_value())
    return redis


def build_storage(redis: Redis) -> BaseStorage:
    storage = RedisStorage(redis)
    return storage
