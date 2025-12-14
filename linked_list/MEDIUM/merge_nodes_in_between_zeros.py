# Merge Nodes in Between Zeros
# Problem: https://leetcode.com/problems/merge-nodes-in-between-zeros/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        sum_val = 0

        while head:
            if head.val == 0:
                if sum_val > 0:
                    current.next = ListNode(sum_val)
                    current = current.next
                    sum_val = 0
            else:
                sum_val += head.val
            head = head.next

        return dummy.next

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([0, 3, 1, 0, 4, 5, 2, 0])
    solution = Solution()
    result = solution.mergeNodes(head)
    print("Merged nodes in between zeros:")
    print_linked_list(result)
