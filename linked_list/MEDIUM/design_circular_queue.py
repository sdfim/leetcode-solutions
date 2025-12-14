# Design Circular Queue
# Problem: https://leetcode.com/problems/design-circular-queue/
# Solution:

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[(self.tail - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

if __name__ == "__main__":
    # Example use case
    circularQueue = MyCircularQueue(3)
    print(circularQueue.enQueue(1))  # True
    print(circularQueue.enQueue(2))  # True
    print(circularQueue.enQueue(3))  # True
    print(circularQueue.enQueue(4))  # False
    print(circularQueue.Rear())      # 3
    print(circularQueue.isFull())    # True
    print(circularQueue.deQueue())   # True
    print(circularQueue.enQueue(4))  # True
    print(circularQueue.Rear())      # 4
