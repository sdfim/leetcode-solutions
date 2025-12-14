# Add Two Numbers
# Problem: https://leetcode.com/problems/add-two-numbers/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

if __name__ == "__main__":
    # Example use case
    list1 = create_linked_list([2, 4, 3])
    list2 = create_linked_list([5, 6, 4])
    solution = Solution()
    result = solution.addTwoNumbers(list1, list2)
    print("Resultant Linked List:")
    print_linked_list(result)
