# Populating Next Right Pointers in Each Node
# Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
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

        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root

if __name__ == "__main__":
    # Example use case
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    solution = Solution()
    connected_root = solution.connect(root)
    print("Next pointers populated.")
