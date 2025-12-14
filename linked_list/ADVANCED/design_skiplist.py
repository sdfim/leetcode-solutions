# Design Skiplist
# Problem: https://leetcode.com/problems/design-skiplist/
# Solution:

import random

class Skiplist:
    def __init__(self):
        self.levels = [[]]

    def search(self, target: int) -> bool:
        for level in reversed(self.levels):
            for num in level:
                if num == target:
                    return True
                if num > target:
                    break
        return False

    def add(self, num: int) -> None:
        for level in self.levels:
            level.append(num)
            level.sort()
        if random.random() < 0.5:
            self.levels.append([])

    def erase(self, num: int) -> bool:
        found = False
        for level in self.levels:
            if num in level:
                level.remove(num)
                found = True
        return found

if __name__ == "__main__":
    # Example use case
    skiplist = Skiplist()
    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    print(skiplist.search(0))  # False
    skiplist.add(4)
    print(skiplist.search(1))  # True
    skiplist.erase(0)          # False
    skiplist.erase(1)          # True
    print(skiplist.search(1))  # False
