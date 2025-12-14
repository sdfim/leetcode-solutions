# Remove Zero Sum Consecutive Nodes from Linked List
# Problem: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        seen = {}
        current = dummy

        while current:
            prefix_sum += current.val
            seen[prefix_sum] = current
            current = current.next

        prefix_sum = 0
        current = dummy
        while current:
            prefix_sum += current.val
            current.next = seen[prefix_sum].next
            current = current.next

        return dummy.next

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([1, 2, -3, 3, 1])
    solution = Solution()
    result = solution.removeZeroSumSublists(head)
    print("Resultant Linked List:")
    print_linked_list(result)
