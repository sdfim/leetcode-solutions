# Add Two Polynomials Represented as Linked Lists
# Problem: https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/
# Solution:

from typing import Optional
from linked_list.utils import ListNode

class Solution:
    def addPolynomials(self, poly1: Optional[ListNode], poly2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while poly1 and poly2:
            if poly1.val[0] == poly2.val[0]:
                current.next = ListNode((poly1.val[0], poly1.val[1] + poly2.val[1]))
                poly1 = poly1.next
                poly2 = poly2.next
            elif poly1.val[0] > poly2.val[0]:
                current.next = ListNode(poly1.val)
                poly1 = poly1.next
            else:
                current.next = ListNode(poly2.val)
                poly2 = poly2.next
            current = current.next

        current.next = poly1 or poly2
        return dummy.next

if __name__ == "__main__":
    # Example use case
    print("Add two polynomials represented as linked lists.")
