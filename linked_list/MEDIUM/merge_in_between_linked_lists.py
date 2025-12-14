# Merge In Between Linked Lists
# Problem: https://leetcode.com/problems/merge-in-between-linked-lists/
# Solution:

from typing import Optional
from linked_list.utils import ListNode

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = list1
        for _ in range(a):
            prev = current
            current = current.next

        for _ in range(b - a + 1):
            current = current.next

        prev.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = current

        return list1

if __name__ == "__main__":
    # Example use case
    print("Merge in between linked lists.")
