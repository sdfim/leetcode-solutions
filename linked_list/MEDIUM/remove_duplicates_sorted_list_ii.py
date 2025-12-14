# Remove Duplicates from Sorted List II
# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next

            head = head.next

        return dummy.next

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([1, 2, 3, 3, 4, 4, 5])
    solution = Solution()
    result = solution.deleteDuplicates(linked_list)
    print("Linked List after removing duplicates:")
    print_linked_list(result)
