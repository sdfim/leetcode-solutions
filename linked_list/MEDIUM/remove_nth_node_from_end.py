# Remove Nth Node From End of List
# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    result = solution.removeNthFromEnd(linked_list, 2)
    print("Linked List after removal:")
    print_linked_list(result)
