# Delete the Middle Node of a Linked List
# Problem: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
            
        slow, fast = head, head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next.next
        return head

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
    
    head1 = create_list([1,3,4,7,1,2,6])
    res1 = solution.deleteMiddle(head1)
    print("Deleted middle:", end=" ")
    print_list(res1)
