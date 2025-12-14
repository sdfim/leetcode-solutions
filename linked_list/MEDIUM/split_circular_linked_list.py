# Split a Circular Linked List
# Problem: https://leetcode.com/problems/split-a-circular-linked-list/
# Solution:

from typing import Optional, Tuple
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def splitCircularLinkedList(self, head: Optional[ListNode]) -> Tuple[Optional[ListNode], Optional[ListNode]]:
        if not head or not head.next:
            return head, None

        slow, fast = head, head
        while fast.next != head and fast.next.next != head:
            slow = slow.next
            fast = fast.next.next

        head1, head2 = head, slow.next
        slow.next = head1

        current = head2
        while current.next != head:
            current = current.next
        current.next = head2

        return head1, head2

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([1, 2, 3, 4, 5])
    head.next.next.next.next.next = head  # Make it circular
    solution = Solution()
    head1, head2 = solution.splitCircularLinkedList(head)
    print("First half of circular linked list:")
    print_linked_list(head1)
    print("Second half of circular linked list:")
    print_linked_list(head2)
