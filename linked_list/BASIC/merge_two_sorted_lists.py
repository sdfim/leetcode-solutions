# Merge Two Sorted Lists
# Problem: https://leetcode.com/problems/merge-two-sorted-lists/
# Solution:

# Updated to ensure consistent problem description and solution structure

from typing import Optional
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next

if __name__ == "__main__":
    # Example use case
    def print_linked_list(head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(" -> ".join(map(str, values)))

    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    solution = Solution()
    print("List 1:")
    print_linked_list(list1)
    print("List 2:")
    print_linked_list(list2)

    merged_list = solution.mergeTwoLists(list1, list2)
    print("Merged List:")
    print_linked_list(merged_list)
