# Middle of the Linked List
# Problem: https://leetcode.com/problems/middle-of-the-linked-list/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == "__main__":
    def create_list(values):
        dummy = ListNode()
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    solution = Solution()
    
    head1 = create_list([1,2,3,4,5])
    mid1 = solution.middleNode(head1)
    print(f"Middle of [1,2,3,4,5]: {mid1.val if mid1 else None}")
    
    head2 = create_list([1,2,3,4,5,6])
    mid2 = solution.middleNode(head2)
    print(f"Middle of [1,2,3,4,5,6]: {mid2.val if mid2 else None}")
