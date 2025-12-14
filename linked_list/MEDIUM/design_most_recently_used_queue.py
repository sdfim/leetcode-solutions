# Design Most Recently Used Queue
# Problem: https://leetcode.com/problems/design-most-recently-used-queue/
# Solution:

from collections import deque

class MRUQueue:

    def __init__(self, n: int):
        self.queue = deque(range(1, n + 1))

    def fetch(self, k: int) -> int:
        value = self.queue[k - 1]
        self.queue.remove(value)
        self.queue.append(value)
        return value

if __name__ == "__main__":
    # Example use case
    mruQueue = MRUQueue(8)
    print(mruQueue.fetch(3))  # 3
    print(mruQueue.fetch(5))  # 6
