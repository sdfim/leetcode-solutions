# Populating Next Right Pointers in Each Node II
# Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Solution:

from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        current = root
        dummy = Node(0)
        tail = dummy

        while current:
            if current.left:
                tail.next = current.left
                tail = tail.next
            if current.right:
                tail.next = current.right
                tail = tail.next
            current = current.next

            if not current:
                current = dummy.next
                dummy.next = None
                tail = dummy

        return root

if __name__ == "__main__":
    # Example use case
    root = Node(1, Node(2, None, Node(5)), Node(3, None, Node(7)))
    solution = Solution()
    connected_root = solution.connect(root)
    print("Next pointers populated for each node.")
