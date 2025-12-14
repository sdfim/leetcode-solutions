# Merge k Sorted Lists
# Problem: https://leetcode.com/problems/merge-k-sorted-lists/
# Solution:

from typing import List, Optional
from linked_list.utils import ListNode, create_linked_list, print_linked_list
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

if __name__ == "__main__":
    # Example use case
    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    solution = Solution()
    result = solution.mergeKLists(lists)
    print("Merged k sorted lists:")
    print_linked_list(result)
