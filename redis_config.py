import yaml
from redisqueue import RedisQueue
from redis import Redis


def get_config():
    with open("redis.yaml") as f:
        return yaml.load(f, yaml.FullLoader)


def get_queue():
    redis_config = get_config()
    return RedisQueue(**redis_config["redis"])


def get_redis():
    redis_config = get_config()
    return Redis(
        host = redis_config["redis"]["host"],
        port = redis_config["redis"]["port"],
        charset = "utf-8",
        decode_responses = True
    )
