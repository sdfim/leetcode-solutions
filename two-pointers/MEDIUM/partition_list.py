# Partition List
# Problem: https://leetcode.com/problems/partition-list/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0) # Store < x
        dummy2 = ListNode(0) # Store >= x
        curr1, curr2 = dummy1, dummy2
        
        while head:
            if head.val < x:
                curr1.next = head
                curr1 = curr1.next
            else:
                curr2.next = head
                curr2 = curr2.next
            head = head.next
            
        curr2.next = None
        curr1.next = dummy2.next
        
        return dummy1.next

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
    
    head1 = create_list([1,4,3,2,5,2])
    x1 = 3
    res1 = solution.partition(head1, x1)
    print(f"Partitioned list around {x1}:", end=" ")
    print_list(res1)
