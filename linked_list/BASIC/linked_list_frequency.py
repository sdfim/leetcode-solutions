# Linked List Frequency
# Problem: Custom Problem
# Solution:

# Updated to ensure consistent problem description and solution structure

from typing import Optional, Dict
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def calculateFrequency(self, head: Optional[ListNode]) -> Dict[int, int]:
        frequency = {}

        while head:
            frequency[head.val] = frequency.get(head.val, 0) + 1
            head = head.next

        return frequency

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([1, 2, 3, 2, 1, 4, 4, 4])
    solution = Solution()
    print("Frequency of elements in Linked List:", solution.calculateFrequency(linked_list))
