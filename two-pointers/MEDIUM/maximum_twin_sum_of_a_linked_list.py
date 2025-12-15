# Maximum Twin Sum of a Linked List
# Problem: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        max_sum = 0
        left, right = head, prev
        while right:
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next
            
        return max_sum

if __name__ == "__main__":
    def create_list(values):
        dummy = ListNode()
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next
        
    solution = Solution()
    
    head1 = create_list([5,4,2,1])
    print(f"Max twin sum [5,4,2,1]: {solution.pairSum(head1)}")
    
    head2 = create_list([4,2,2,3])
    print(f"Max twin sum [4,2,2,3]: {solution.pairSum(head2)}")
