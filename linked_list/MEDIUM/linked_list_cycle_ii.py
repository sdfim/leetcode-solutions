# Linked List Cycle II
# Problem: https://leetcode.com/problems/linked-list-cycle-ii/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        while head != slow:
            head = head.next
            slow = slow.next

        return head

if __name__ == "__main__":
    # Example use case
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle here
    solution = Solution()
    cycle_node = solution.detectCycle(node1)
    print(f"Cycle starts at node with value: {cycle_node.val if cycle_node else 'No cycle'}")
