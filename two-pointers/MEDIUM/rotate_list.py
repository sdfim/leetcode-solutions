# Rotate List
# Problem: https://leetcode.com/problems/rotate-list/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
            
        # 1. Compute length and make it circular
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        tail.next = head # Circle
        
        # 2. Find new tail position
        k = k % length
        steps_to_new_tail = length - k
        
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None # Break circle
        
        return new_head

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
    
    head1 = create_list([1,2,3,4,5])
    print("Original:", end=" ")
    print_list(head1)
    
    res1 = solution.rotateRight(head1, 2)
    print("Rotated by 2:", end=" ")
    print_list(res1)
