# Flatten Binary Tree to Linked List
# Problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Solution:

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        temp = root.right
        root.right = root.left
        root.left = None

        current = root
        while current.right:
            current = current.right

        current.right = temp

if __name__ == "__main__":
    # Example use case
    tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    solution = Solution()
    solution.flatten(tree)
    print("Binary tree flattened to linked list.")
