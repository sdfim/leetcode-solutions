# Odd Even Linked List
# Problem: https://leetcode.com/problems/odd-even-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    result = solution.oddEvenList(linked_list)
    print("Odd Even Linked List:")
    print_linked_list(result)
