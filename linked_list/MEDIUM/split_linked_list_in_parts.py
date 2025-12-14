# Split Linked List in Parts
# Problem: https://leetcode.com/problems/split-linked-list-in-parts/
# Solution:

from typing import List, Optional
from linked_list.utils import ListNode

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        part_size, extra = divmod(length, k)
        parts = []
        current = head

        for i in range(k):
            part_head = current
            for j in range(part_size + (i < extra) - 1):
                if current:
                    current = current.next
            if current:
                next_part, current.next = current.next, None
                current = next_part
            parts.append(part_head)

        return parts

if __name__ == "__main__":
    # Example use case
    from linked_list.utils import create_linked_list, print_linked_list
    head = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    parts = solution.splitListToParts(head, 3)
    for i, part in enumerate(parts):
        print(f"Part {i + 1}:")
        print_linked_list(part)
