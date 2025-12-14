# Swapping Nodes in a Linked List
# Problem: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first, second, current = None, None, head
        count = 1

        while current:
            if count == k:
                first = current
            if count > k:
                if not second:
                    second = head
                else:
                    second = second.next
            count += 1
            current = current.next

        if first and second:
            first.val, second.val = second.val, first.val

        return head

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    result = solution.swapNodes(head, 2)
    print("Swapped nodes in linked list:")
    print_linked_list(result)
