# Reverse Nodes in Even Length Groups
# Problem: https://leetcode.com/problems/reverse-nodes-in-even-length-groups/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(start, end):
            prev, current = None, start
            while current != end:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head
        group_size = 1

        while current:
            start = current
            for _ in range(group_size):
                if not current.next:
                    break
                current = current.next

            next_group = current.next
            if (group_size % 2) == 0:
                prev.next = reverse(start, next_group)
                start.next = next_group
            prev, current = start, next_group
            group_size += 1

        return dummy.next

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    solution = Solution()
    result = solution.reverseEvenLengthGroups(head)
    print("Reversed nodes in even length groups:")
    print_linked_list(result)
