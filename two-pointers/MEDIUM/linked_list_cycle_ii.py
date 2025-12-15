# Linked List Cycle II
# Problem: https://leetcode.com/problems/linked-list-cycle-ii/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Cycle detected
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
                
        return None

if __name__ == "__main__":
    solution = Solution()
    
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 # Cycle back to node 2
    
    cycle_node = solution.detectCycle(node1)
    print(f"Cycle begins at node with value: {cycle_node.val if cycle_node else 'No Cycle'}")
