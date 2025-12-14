# Copy List with Random Pointer
# Problem: https://leetcode.com/problems/copy-list-with-random-pointer/
# Solution:

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}
        current = head

        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            old_to_new[current].next = old_to_new.get(current.next)
            old_to_new[current].random = old_to_new.get(current.random)
            current = current.next

        return old_to_new[head]

if __name__ == "__main__":
    # Example use case
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node1.next = node2
    node2.next = node3
    node2.random = node1
    solution = Solution()
    copied_list = solution.copyRandomList(node1)
    print("List with random pointers copied.")
