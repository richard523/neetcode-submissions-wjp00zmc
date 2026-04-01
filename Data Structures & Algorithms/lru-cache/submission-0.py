class LRUCache:
    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        for i in range(len(self.cache)): #loop through
            if self.cache[i][0] == key: #if value matches target get
                tmp = self.cache.pop(i) #remove current value
                self.cache.append(tmp) #append it to END. first index is LRU
                return tmp[1] #return value of tmp (currently (i, v))
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)): #loop through cache
            if self.cache[i][0] == key: #if value matches target put
                tmp = self.cache.pop(i) #remove val
                tmp[1] = value #update value
                self.cache.append(tmp) #append to end
                return
        #no matching key was found.
        if self.capacity == len(self.cache): #if capacity is full, pop.
            self.cache.pop(0)
        
        self.cache.append([key,value])