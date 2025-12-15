# Swapping Nodes in a Linked List
# Problem: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        # Identify nodes to swap
        # 1-indexed k
        # First node is at index k
        # Second node is at index length - k + 1
        
        first_k = head
        for _ in range(k - 1):
            first_k = first_k.next
            
        second_k = head
        for _ in range(length - k):
            second_k = second_k.next
            
        # Swap values
        first_k.val, second_k.val = second_k.val, first_k.val
        
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
    
    head1 = create_list([1,2,3,4,5])
    k1 = 2
    res1 = solution.swapNodes(head1, k1)
    print("Swapped:", end=" ")
    print_list(res1)
