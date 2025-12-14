# Insert into a Sorted Circular Linked List
# Problem: https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
# Solution:

from typing import Optional
from linked_list.utils import ListNode

class Solution:
    def insert(self, head: Optional[ListNode], insertVal: int) -> Optional[ListNode]:
        new_node = ListNode(insertVal)
        if not head:
            new_node.next = new_node
            return new_node

        prev, curr = head, head.next
        while True:
            if prev.val <= insertVal <= curr.val:
                break
            if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
                break
            prev, curr = curr, curr.next
            if prev == head:
                break

        prev.next = new_node
        new_node.next = curr
        return head

if __name__ == "__main__":
    # Example use case
    node1 = ListNode(3)
    node2 = ListNode(4)
    node3 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node1
    solution = Solution()
    updated_list = solution.insert(node1, 2)
    print("Inserted into sorted circular linked list.")
