# Partition List
# Problem: https://leetcode.com/problems/partition-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next
        return before_head.next

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([1, 4, 3, 2, 5, 2])
    solution = Solution()
    result = solution.partition(linked_list, 3)
    print("Partitioned Linked List:")
    print_linked_list(result)
