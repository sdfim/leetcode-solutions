# All O`one Data Structure
# Problem: https://leetcode.com/problems/all-oone-data-structure/
# Solution:

class AllOne:
    def __init__(self):
        self.key_count = {}
        self.count_keys = {}
        self.min_count = None
        self.max_count = None

    def inc(self, key: str) -> None:
        count = self.key_count.get(key, 0)
        self.key_count[key] = count + 1
        if count in self.count_keys:
            self.count_keys[count].remove(key)
            if not self.count_keys[count]:
                del self.count_keys[count]
        self.count_keys.setdefault(count + 1, set()).add(key)
        self.min_count = min(self.count_keys.keys())
        self.max_count = max(self.count_keys.keys())

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return
        count = self.key_count[key]
        if count == 1:
            del self.key_count[key]
        else:
            self.key_count[key] = count - 1
        self.count_keys[count].remove(key)
        if not self.count_keys[count]:
            del self.count_keys[count]
        if count > 1:
            self.count_keys.setdefault(count - 1, set()).add(key)
        self.min_count = min(self.count_keys.keys(), default=None)
        self.max_count = max(self.count_keys.keys(), default=None)

    def getMaxKey(self) -> str:
        if not self.max_count:
            return ""
        return next(iter(self.count_keys[self.max_count]))

    def getMinKey(self) -> str:
        if not self.min_count:
            return ""
        return next(iter(self.count_keys[self.min_count]))

if __name__ == "__main__":
    # Example use case
    all_one = AllOne()
    all_one.inc("hello")
    all_one.inc("world")
    all_one.inc("hello")
    print(all_one.getMaxKey())  # "hello"
    print(all_one.getMinKey())  # "world"
    all_one.dec("hello")
    print(all_one.getMaxKey())  # "hello"
    print(all_one.getMinKey())  # "world"
