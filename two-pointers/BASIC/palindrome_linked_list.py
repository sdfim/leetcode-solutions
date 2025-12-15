# Palindrome Linked List
# Problem: https://leetcode.com/problems/palindrome-linked-list/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
            
        # 1. Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        # 3. Compare halves
        left, right = head, prev
        while right: # right is shorter or equal to left
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True

if __name__ == "__main__":
    def create_list(values):
        dummy = ListNode()
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    solution = Solution()
    
    head1 = create_list([1,2,2,1])
    print(f"Is palindrome [1,2,2,1]: {solution.isPalindrome(head1)}")
    
    head2 = create_list([1,2])
    print(f"Is palindrome [1,2]: {solution.isPalindrome(head2)}")
