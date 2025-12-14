# Design Circular Deque
# Problem: https://leetcode.com/problems/design-circular-deque/
# Solution:

class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1) % self.capacity
        self.queue[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.queue[(self.tail - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

if __name__ == "__main__":
    # Example use case
    circularDeque = MyCircularDeque(3)
    print(circularDeque.insertLast(1))  # True
    print(circularDeque.insertLast(2))  # True
    print(circularDeque.insertFront(3)) # True
    print(circularDeque.insertFront(4)) # False
    print(circularDeque.getRear())      # 2
    print(circularDeque.isFull())       # True
    print(circularDeque.deleteLast())   # True
    print(circularDeque.insertFront(4)) # True
    print(circularDeque.getFront())     # 4
