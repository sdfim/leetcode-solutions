# Delete the Middle Node of a Linked List
# Problem: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    result = solution.deleteMiddle(head)
    print("Deleted middle node of linked list:")
    print_linked_list(result)
