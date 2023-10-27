if __name__ == "__main__":
	from redis_config import get_queue, get_redis
	q = get_queue()
	redis = get_redis()

	# message get
	# import json
	import time as pytime
	
	while True:
		msg = q.get(is_blocking = True) # 큐가 비어있을 때 대기
		if msg is not None:
			# msg_json = json.loads(msg.decode('utf-8'))
			# print(msg_json)
			# publish_cnt = redis.publish("Pilot Channel1", msg_json)
			publish_cnt = redis.publish("Pilot Channel1", msg)
			print(publish_cnt)
			pytime.sleep(3)