# Two Sum BSTs
# Problem: https://leetcode.com/problems/two-sum-bsts/
# Solution:

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def find(node, val):
            if not node:
                return False
            if node.val == val:
                return True
            if val < node.val:
                return find(node.left, val)
            return find(node.right, val)
            
        stack = [root1]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if find(root2, target - node.val):
                return True
            stack.append(node.left)
            stack.append(node.right)
            
        return False

if __name__ == "__main__":
    solution = Solution()
    
    # Tree 1:   2
    #          / \
    #         1   4
    root1 = TreeNode(2, TreeNode(1), TreeNode(4))
    
    # Tree 2:   1
    #          / \
    #         0   3
    root2 = TreeNode(1, TreeNode(0), TreeNode(3))
    
    target = 5
    print(f"Target {target} found in BSTs: {solution.twoSumBSTs(root1, root2, target)}")
