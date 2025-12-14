# Design Front Middle Back Queue
# Problem: https://leetcode.com/problems/design-front-middle-back-queue/
# Solution:

from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = deque()

    def pushFront(self, val: int) -> None:
        self.queue.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        mid = len(self.queue) // 2
        self.queue.insert(mid, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        return self.queue.popleft() if self.queue else -1

    def popMiddle(self) -> int:
        if not self.queue:
            return -1
        mid = (len(self.queue) - 1) // 2
        return self.queue.pop(mid)

    def popBack(self) -> int:
        return self.queue.pop() if self.queue else -1

if __name__ == "__main__":
    # Example use case
    queue = FrontMiddleBackQueue()
    queue.pushFront(1)
    queue.pushBack(2)
    queue.pushMiddle(3)
    print(queue.popMiddle())  # 3
