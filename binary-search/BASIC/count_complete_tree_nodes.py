# Count Complete Tree Nodes
# Problem: https://leetcode.com/problems/count-complete-tree-nodes/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        def get_depth(node):
            d = 0
            while node:
                d += 1
                node = node.left
            return d
            
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        
        if left_depth == right_depth:
            # Left subtree is a full binary tree
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Right subtree is a full binary tree (one level shallower)
            return (1 << right_depth) + self.countNodes(root.left)

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    print(solution.countNodes(root))  # Output: 6
