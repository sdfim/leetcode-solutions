# Middle of the Linked List
# Problem: https://leetcode.com/problems/middle-of-the-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

if __name__ == "__main__":
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    middle = solution.middleNode(linked_list)
    print("Middle Node Value:", middle.val if middle else None)
