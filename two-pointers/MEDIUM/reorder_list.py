# Reorder List
# Problem: https://leetcode.com/problems/reorder-list/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # 1. Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse second half
        second = slow.next
        slow.next = None # split
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # 3. Merge two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

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
    
    head1 = create_list([1,2,3,4])
    solution.reorderList(head1)
    print("Reordered [1,2,3,4]:", end=" ")
    print_list(head1)
    
    head2 = create_list([1,2,3,4,5])
    solution.reorderList(head2)
    print("Reordered [1,2,3,4,5]:", end=" ")
    print_list(head2)
