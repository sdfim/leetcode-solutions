# Closest Binary Search Tree Value
# Problem: https://leetcode.com/problems/closest-binary-search-tree-value/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        curr = root
        
        while curr:
            if abs(target - curr.val) < abs(target - closest):
                closest = curr.val
            elif abs(target - curr.val) == abs(target - closest):
                closest = min(closest, curr.val)
                
            if target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
                
        return closest

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    print(solution.closestValue(root, 3.714286))  # Output: 4
