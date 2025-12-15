# Split a Circular Linked List
# Problem: https://leetcode.com/problems/split-a-circular-linked-list/
# Solution:

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitCircularLinkedList(self, list_node: Optional[ListNode]) -> List[Optional[ListNode]]:
        if not list_node:
            return [None, None]
            
        slow = fast = list_node
        
        # Find end and length/middle
        while fast.next != list_node and fast.next.next != list_node:
            slow = slow.next
            fast = fast.next.next
            
        if fast.next != list_node: # Even elements case, fast moved one more step
            fast = fast.next
            
        # slow is at end of first half
        # fast is at end of second half (last node)
        
        head1 = list_node
        head2 = slow.next
        
        slow.next = head1
        fast.next = head2
        
        return [head1, head2]

if __name__ == "__main__":
    def create_circular(values):
        dummy = ListNode()
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        curr.next = dummy.next
        return dummy.next
        
    def print_circular(head):
        if not head:
            return
        vals = []
        curr = head
        while True:
            vals.append(curr.val)
            curr = curr.next
            if curr == head:
                break
        print(vals)
        
    solution = Solution()
    
    l1 = create_circular([1,5,7])
    res1 = solution.splitCircularLinkedList(l1)
    print("Split 1:", end=" ")
    print_circular(res1[0])
    print("Split 2:", end=" ")
    print_circular(res1[1])
