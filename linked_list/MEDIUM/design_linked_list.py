# Design Linked List
# Problem: https://leetcode.com/problems/design-linked-list/
# Solution:

class MyLinkedList:
    class Node:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        for _ in range(index):
            if not current:
                return -1
            current = current.next
        return current.val if current else -1

    def addAtHead(self, val: int) -> None:
        new_node = self.Node(val, self.head)
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = self.Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        current = self.head
        for _ in range(index - 1):
            if not current:
                return
            current = current.next
        if current:
            new_node = self.Node(val, current.next)
            current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next if self.head else None
            return
        current = self.head
        for _ in range(index - 1):
            if not current or not current.next:
                return
            current = current.next
        if current and current.next:
            current.next = current.next.next

if __name__ == "__main__":
    # Example use case
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)  # linked list becomes 1->2->3
    print(linkedList.get(1))     # 2
    linkedList.deleteAtIndex(1)  # now the linked list is 1->3
    print(linkedList.get(1))     # 3
