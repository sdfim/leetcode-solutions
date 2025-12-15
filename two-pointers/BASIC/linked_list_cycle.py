# Linked List Cycle
# Problem: https://leetcode.com/problems/linked-list-cycle/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        return False

if __name__ == "__main__":
    solution = Solution()
    
    # Test case: 3 -> 2 -> 0 -> -4 -> (back to 2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 # Cycle
    
    print(f"Has cycle: {solution.hasCycle(node1)}")
    
    # No cycle
    nodeA = ListNode(1)
    print(f"Has cycle: {solution.hasCycle(nodeA)}")
