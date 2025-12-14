# Linked List Components
# Problem: https://leetcode.com/problems/linked-list-components/
# Solution:

from typing import List, Optional
from linked_list.utils import ListNode

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        current = head
        count = 0

        while current:
            if current.val in num_set and (not current.next or current.next.val not in num_set):
                count += 1
            current = current.next

        return count

if __name__ == "__main__":
    # Example use case
    from linked_list.utils import create_linked_list
    head = create_linked_list([0, 1, 2, 3, 4])
    nums = [0, 3, 1, 4]
    solution = Solution()
    result = solution.numComponents(head, nums)
    print(f"Number of components: {result}")
