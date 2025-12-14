# LRU Cache
# Problem: https://leetcode.com/problems/lru-cache/
# Solution:

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

if __name__ == "__main__":
    # Example use case
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))  # 1
    lru.put(3, 3)      # evicts key 2
    print(lru.get(2))  # -1
    lru.put(4, 4)      # evicts key 1
    print(lru.get(1))  # -1
    print(lru.get(3))  # 3
    print(lru.get(4))  # 4
