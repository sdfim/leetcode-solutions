# Insertion Sort List
# Problem: https://leetcode.com/problems/insertion-sort-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = head

        while current:
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            temp = current.next
            current.next = prev.next
            prev.next = current
            current = temp

        return dummy.next

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([4, 2, 1, 3])
    solution = Solution()
    sorted_list = solution.insertionSortList(linked_list)
    print("Sorted Linked List:")
    print_linked_list(sorted_list)
