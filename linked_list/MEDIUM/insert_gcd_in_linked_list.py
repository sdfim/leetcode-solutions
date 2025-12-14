# Insert Greatest Common Divisors in Linked List
# Problem: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
# Solution:

from math import gcd
from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            gcd_val = gcd(current.val, current.next.val)
            new_node = ListNode(gcd_val, current.next)
            current.next = new_node
            current = new_node.next

        return head

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([18, 6, 10, 3])
    solution = Solution()
    result = solution.insertGreatestCommonDivisors(head)
    print("Inserted GCDs in linked list:")
    print_linked_list(result)
