# Remove Duplicates From an Unsorted Linked List
# Problem: https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def removeDuplicatesUnsorted(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head

        while current:
            if current.val in seen:
                prev.next = current.next
            else:
                seen.add(current.val)
                prev = current
            current = current.next

        return dummy.next

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([1, 2, 3, 2, 1])
    solution = Solution()
    result = solution.removeDuplicatesUnsorted(head)
    print("Removed duplicates from unsorted linked list:")
    print_linked_list(result)
