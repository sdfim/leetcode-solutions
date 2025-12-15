# Two Sum BSTs
# Problem: https://leetcode.com/problems/two-sum-bsts/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        # Traverse tree1, for each node, search (target - node.val) in tree2.
        
        def search(node, val):
            while node:
                if node.val == val:
                    return True
                elif val < node.val:
                    node = node.left
                else:
                    node = node.right
            return False
            
        stack = [root1]
        while stack:
            node = stack.pop()
            if not node:
                continue
            
            complement = target - node.val
            if search(root2, complement):
                return True
                
            stack.append(node.left)
            stack.append(node.right)
            
        return False
