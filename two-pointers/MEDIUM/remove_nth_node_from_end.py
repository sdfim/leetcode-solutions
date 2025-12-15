# Remove Nth Node From End of List
# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
            
        while right:
            left = left.next
            right = right.next
            
        # Delete node
        left.next = left.next.next
        
        return dummy.next

if __name__ == "__main__":
    def create_list(values):
        dummy = ListNode()
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next
    
    def print_list(head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        print(vals)
        
    solution = Solution()
    
    # Test cases
    head1 = create_list([1,2,3,4,5])
    print("Original:", end=" ")
    print_list(head1)
    res1 = solution.removeNthFromEnd(head1, 2)
    print("After removing 2nd from end:", end=" ")
    print_list(res1)
