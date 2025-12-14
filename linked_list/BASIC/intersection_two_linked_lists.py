# Intersection of Two Linked Lists
# Problem: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Solution:

# Updated to ensure consistent problem description and solution structure

from typing import Optional
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a

if __name__ == "__main__":
    # Create two intersecting linked lists
    common = create_linked_list([8, 4, 5])
    listA = ListNode(4, ListNode(1, common))
    listB = ListNode(5, ListNode(6, ListNode(1, common)))

    solution = Solution()
    intersection = solution.getIntersectionNode(listA, listB)
    print("Intersection Node Value:", intersection.val if intersection else None)
