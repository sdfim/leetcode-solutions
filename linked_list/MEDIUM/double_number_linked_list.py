# Double a Number Represented as a Linked List
# Problem: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current, carry = head, 0

        while current:
            current.val = current.val * 2 + carry
            carry = current.val // 10
            current.val %= 10
            if not current.next and carry:
                current.next = ListNode(carry)
                break
            current = current.next

        return head

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([1, 2, 3])
    solution = Solution()
    result = solution.doubleIt(head)
    print("Doubled number represented as linked list:")
    print_linked_list(result)
