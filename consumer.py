if __name__ == "__main__":
    from redis_config import get_redis
    redis_db = get_redis()

    pubsub = redis_db.pubsub()
    subs = pubsub.subscribe("Pilot Channel1")

    for message in pubsub.listen():
        if message.get("type") == "message":
            print(message, message.get("data"))
