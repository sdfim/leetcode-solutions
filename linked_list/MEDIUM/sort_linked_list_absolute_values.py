# Sort Linked List Already Sorted Using Absolute Values
# Problem: https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head

        while current and current.next:
            if current.next.val < 0:
                temp = current.next
                current.next = temp.next
                temp.next = dummy.next
                dummy.next = temp
            else:
                current = current.next

        return dummy.next

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([1, -2, -3, 4, -5])
    solution = Solution()
    result = solution.sortLinkedList(head)
    print("Sorted linked list by absolute values:")
    print_linked_list(result)
