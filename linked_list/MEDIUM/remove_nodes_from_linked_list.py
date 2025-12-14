# Remove Nodes From Linked List
# Problem: https://leetcode.com/problems/remove-nodes-from-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        while current:
            while stack and stack[-1].val < current.val:
                stack.pop()
            stack.append(current)
            current = current.next

        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        stack[-1].next = None

        return stack[0] if stack else None

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([5, 2, 13, 3, 8])
    solution = Solution()
    result = solution.removeNodes(head)
    print("Removed nodes from linked list:")
    print_linked_list(result)
