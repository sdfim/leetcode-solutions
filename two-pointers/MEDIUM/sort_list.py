# Sort List
# Problem: https://leetcode.com/problems/sort-list/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        # 1. Split list into two halves
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        # 2. Sort both halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # 3. Merge sorted halves
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
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
    
    head1 = create_list([4,2,1,3])
    res1 = solution.sortList(head1)
    print("Sorted list:", end=" ")
    print_list(res1)
