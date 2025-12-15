# Intersection of Two Linked Lists
# Problem: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
            
        pA = headA
        pB = headB
        
        while pA != pB:
            pA = headA if pA is None else pA.next
            pB = headB if pB is None else pB.next
            
        return pA

if __name__ == "__main__":
    solution = Solution()
    
    # Test case
    # List A: 4 -> 1 -\
    #                  8 -> 4 -> 5
    # List B: 5 -> 6 -/
    
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)
    
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common
    
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = common
    
    intersection = solution.getIntersectionNode(headA, headB)
    print(f"Intersection Val: {intersection.val if intersection else 'None'}")
