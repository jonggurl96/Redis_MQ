if __name__ == "__main__":
	from redis_config import get_queue
	q = get_queue()
	
	# message put
	import json
	import time as pytime
	
	for i in range(30):
		cur_time = f'{{"timestamp": {pytime.time()}}}'
		element = json.loads(cur_time)

		element_str = json.dumps(element)
		print(element_str)
		q.put(element_str)
	