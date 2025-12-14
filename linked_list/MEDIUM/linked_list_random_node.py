# Linked List Random Node
# Problem: https://leetcode.com/problems/linked-list-random-node/
# Solution:

import random
from typing import Optional
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.nodes = []
        while head:
            self.nodes.append(head)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.nodes).val

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution(linked_list)
    print("Random node value:", solution.getRandom())
