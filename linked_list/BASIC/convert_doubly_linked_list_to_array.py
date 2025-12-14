from typing import Optional, List
from linked_list.utils import ListNode, create_linked_list, print_linked_list

# Problem: Custom Problem
# Solution:

class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def convertToArray(self, head: Optional[DoublyListNode]) -> List[int]:
        result = []

        while head:
            result.append(head.val)
            head = head.next

        return result

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    print("Converted to Array:", solution.convertToArray(linked_list))
