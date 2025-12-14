# Remove Linked List Elements
# Problem: https://leetcode.com/problems/remove-linked-list-elements/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next

if __name__ == "__main__":
    # Example use case
    def print_linked_list(head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(" -> ".join(map(str, values)))

    linked_list = create_linked_list([1, 2, 6, 3, 4, 5, 6])
    solution = Solution()
    print("Original Linked List:")
    print_linked_list(linked_list)

    modified_list = solution.removeElements(linked_list, 6)
    print("Linked List after Removing Elements:")
    print_linked_list(modified_list)
