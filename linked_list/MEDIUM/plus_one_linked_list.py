# Plus One Linked List
# Problem: https://leetcode.com/problems/plus-one-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def plusOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        head = reverse(head)
        current = head
        carry = 1

        while current and carry:
            current.val += carry
            carry = current.val // 10
            current.val %= 10
            if not current.next and carry:
                current.next = ListNode(0)
            current = current.next

        head = reverse(head)
        return head

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([1, 2, 3])
    solution = Solution()
    result = solution.plusOne(linked_list)
    print("Linked List after plus one:")
    print_linked_list(result)
