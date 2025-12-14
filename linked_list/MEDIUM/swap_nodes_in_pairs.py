# Swap Nodes in Pairs
# Problem: https://leetcode.com/problems/swap-nodes-in-pairs/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, current = dummy, head

        while current and current.next:
            next_pair = current.next.next
            second = current.next

            second.next = current
            current.next = next_pair
            prev.next = second

            prev = current
            current = next_pair

        return dummy.next

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([1, 2, 3, 4])
    solution = Solution()
    result = solution.swapPairs(linked_list)
    print("Linked List after swapping pairs:")
    print_linked_list(result)
