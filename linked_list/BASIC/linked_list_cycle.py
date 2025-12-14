from linked_list.utils import ListNode, create_linked_list

# Problem: https://leetcode.com/problems/linked-list-cycle/
# Solution:

# Updated to ensure consistent problem description and solution structure

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([3, 2, 0, -4])
    solution = Solution()
    print("Linked List Created")
