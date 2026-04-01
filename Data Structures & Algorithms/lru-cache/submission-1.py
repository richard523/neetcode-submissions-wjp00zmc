class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) #doubly linked list. get relinked s/t its moved to end. MRU
        return self.cache[key]
    def put(self, key: int, value: int) -> None:
        if key in self.cache: #if key is in cache
            self.cache.move_to_end(key) #move key to end, MRU
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

