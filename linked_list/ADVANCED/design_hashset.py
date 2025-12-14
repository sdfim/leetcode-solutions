# Design HashSet
# Problem: https://leetcode.com/problems/design-hashset/
# Solution:

class MyHashSet:
    def __init__(self):
        self.bucket = [False] * 1000001

    def add(self, key: int) -> None:
        self.bucket[key] = True

    def remove(self, key: int) -> None:
        self.bucket[key] = False

    def contains(self, key: int) -> bool:
        return self.bucket[key]

if __name__ == "__main__":
    # Example use case
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    print(hashSet.contains(1))  # True
    print(hashSet.contains(3))  # False
    hashSet.add(2)
    print(hashSet.contains(2))  # True
    hashSet.remove(2)
    print(hashSet.contains(2))  # False
