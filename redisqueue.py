import redis

class RedisQueue:
	"""
		Redis Lists are an ordered list, FIFO Queue
		Redis List pushing new elements on the head of the list.
		The max length of a list is 4,294,967,295
	"""
	
	def __init__(self, name, **redis_kwargs):
		"""
		:param name: queue name
		:param redis_kwargs: localhost:6379/0(default)
		"""
		self.key = name
		self.rq = redis.Redis(**redis_kwargs)
	
	def size(self):
		return self.rq.llen(self.key)
	
	def is_empty(self):
		return self.size() == 0
	
	def put(self, element):
		self.rq.lpush(self.key, element) # left push
	
	def get(self, is_blocking = False, timeout = None):
		if is_blocking:
			element = self.rq.brpop(self.key, timeout = timeout) # blocking right pop, return (K, V)
			
			element = element[1]
		
		else:
			element = self.rq.rpop(self.key) # right pop
		
		return element
	
	
	def get_without_pop(self): # 꺼낼 데이터 조회
		return None if self.is_empty() else self.rq.lindex(self.key, -1)