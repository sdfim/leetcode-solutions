# Convert Binary Number in a Linked List to Integer
# Problem: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0

        while head:
            num = num * 2 + head.val
            head = head.next

        return num

if __name__ == "__main__":
    # Example use case
    binary_list = create_linked_list([1, 0, 1])
    solution = Solution()
    print("Binary Linked List to Integer:", solution.getDecimalValue(binary_list))
