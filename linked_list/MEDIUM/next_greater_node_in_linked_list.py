# Next Greater Node In Linked List
# Problem: https://leetcode.com/problems/next-greater-node-in-linked-list/
# Solution:

from typing import List, Optional
from linked_list.utils import ListNode

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        result = []
        current = head

        while current:
            result.append(current.val)
            current = current.next

        for i in range(len(result) - 1, -1, -1):
            while stack and stack[-1] <= result[i]:
                stack.pop()
            stack.append(result[i])
            result[i] = stack[-1] if stack else 0

        return result

if __name__ == "__main__":
    # Example use case
    from linked_list.utils import create_linked_list
    head = create_linked_list([2, 1, 5])
    solution = Solution()
    result = solution.nextLargerNodes(head)
    print(f"Next greater nodes: {result}")
