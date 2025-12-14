# Maximum Twin Sum of a Linked List
# Problem: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        max_sum = 0
        while slow:
            max_sum = max(max_sum, slow.val + stack.pop())
            slow = slow.next

        return max_sum

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([5, 4, 2, 1])
    solution = Solution()
    result = solution.pairSum(head)
    print(f"Maximum twin sum: {result}")
