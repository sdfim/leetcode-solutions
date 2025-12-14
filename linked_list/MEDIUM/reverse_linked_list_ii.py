# Reverse Linked List II
# Problem: https://leetcode.com/problems/reverse-linked-list-ii/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next
        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    result = solution.reverseBetween(linked_list, 2, 4)
    print("Reversed Linked List:")
    print_linked_list(result)
