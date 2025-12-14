# Convert Doubly Linked List to Array II
# Problem: https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/
# Solution:

from typing import List

class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def convertToArray(self, head: DoublyListNode) -> List[int]:
        result = []
        current = head

        while current:
            result.append(current.val)
            current = current.next

        return result

if __name__ == "__main__":
    # Example use case
    node1 = DoublyListNode(1)
    node2 = DoublyListNode(2)
    node3 = DoublyListNode(3)
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2

    solution = Solution()
    result = solution.convertToArray(node1)
    print(f"Converted doubly linked list to array: {result}")
