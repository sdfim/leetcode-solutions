# Remove Duplicates from Sorted List
# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

if __name__ == "__main__":
    # Example use case
    def print_linked_list(head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(" -> ".join(map(str, values)))

    linked_list = create_linked_list([1, 1, 2, 3, 3])
    solution = Solution()
    print("Original Linked List:")
    print_linked_list(linked_list)

    modified_list = solution.deleteDuplicates(linked_list)
    print("Linked List after Removing Duplicates:")
    print_linked_list(modified_list)
