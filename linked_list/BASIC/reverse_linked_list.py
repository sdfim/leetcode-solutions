# Reverse Linked List
# Problem: https://leetcode.com/problems/reverse-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

if __name__ == "__main__":
    # Example use case
    def print_linked_list(head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(" -> ".join(map(str, values)))

    linked_list = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    print("Original Linked List:")
    print_linked_list(linked_list)

    reversed_list = solution.reverseList(linked_list)
    print("Reversed Linked List:")
    print_linked_list(reversed_list)
