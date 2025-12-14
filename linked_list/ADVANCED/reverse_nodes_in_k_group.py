# Reverse Nodes in k-Group
# Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            prev, current = None, start
            while current != end:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            reverse(group_prev.next, group_next)

            temp = group_prev.next
            group_prev.next = kth
            temp.next = group_next
            group_prev = temp

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    result = solution.reverseKGroup(head, 2)
    print("Reversed nodes in k-group:")
    print_linked_list(result)
