# Delete N Nodes After M Nodes of a Linked List
# Problem: https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        current = head

        while current:
            # Skip m nodes
            for _ in range(m - 1):
                if not current:
                    return head
                current = current.next

            # Delete n nodes
            temp = current.next
            for _ in range(n):
                if temp:
                    temp = temp.next

            # Connect the remaining part
            if current:
                current.next = temp
                current = temp

        return head

if __name__ == "__main__":
    linked_list = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    solution = Solution()
    print("Original Linked List:")
    print_linked_list(linked_list)

    modified_list = solution.deleteNodes(linked_list, 2, 3)
    print("Modified Linked List:")
    print_linked_list(modified_list)
