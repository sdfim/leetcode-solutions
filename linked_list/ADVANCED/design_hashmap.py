# Design HashMap
# Problem: https://leetcode.com/problems/design-hashmap/
# Solution:

class MyHashMap:
    def __init__(self):
        self.bucket = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.bucket[key] = value

    def get(self, key: int) -> int:
        return self.bucket[key]

    def remove(self, key: int) -> None:
        self.bucket[key] = -1

if __name__ == "__main__":
    # Example use case
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    print(hashMap.get(1))  # 1
    print(hashMap.get(3))  # -1
    hashMap.put(2, 1)
    print(hashMap.get(2))  # 1
    hashMap.remove(2)
    print(hashMap.get(2))  # -1
