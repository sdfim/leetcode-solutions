# Sort List
# Problem: https://leetcode.com/problems/sort-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid

        def merge(l1, l2):
            dummy = ListNode()
            current = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 or l2
            return dummy.next

        left, right = split(head)
        left = self.sortList(left)
        right = self.sortList(right)
        return merge(left, right)

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([4, 2, 1, 3])
    solution = Solution()
    sorted_list = solution.sortList(linked_list)
    print("Sorted Linked List:")
    print_linked_list(sorted_list)
