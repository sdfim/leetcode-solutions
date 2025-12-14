# Reorder List
# Problem: https://leetcode.com/problems/reorder-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, current = None, slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([1, 2, 3, 4])
    solution = Solution()
    solution.reorderList(linked_list)
    print("Reordered Linked List:")
    print_linked_list(linked_list)
