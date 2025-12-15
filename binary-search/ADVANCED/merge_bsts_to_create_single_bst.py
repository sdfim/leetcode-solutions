# Merge BSTs to Create Single BST
# Problem: https://leetcode.com/problems/merge-bsts-to-create-single-bst/
# (LC 1932)

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        # Hash map: leaf value -> tree index (or node parent info?)
        # Root value -> tree object.
        root_map = {}
        for t in trees:
            root_map[t.val] = t
            
        # Count in-degrees of root nodes to find the supreme root.
        # A root is a child in another tree?
        # Traverse all trees to track leaves.
        
        leaves_present = set()
        
        for t in trees:
             # Traverse t
             stack = [t]
             while stack:
                 node = stack.pop()
                 if node.left:
                     leaves_present.add(node.left.val)
                     stack.append(node.left)
                 if node.right:
                     leaves_present.add(node.right.val)
                     stack.append(node.right)
                     
        # Potential overall root
        super_roots = []
        for t in trees:
            if t.val not in leaves_present:
                super_roots.append(t)
        
        if len(super_roots) != 1:
            return None
        
        root = super_roots[0]
        
        # Merge process
        # Iterate standard tree traversal.
        # If we reach a leaf, check if there is a pending tree with that root.
        # If so, attach.
        # Keep track of visited bounds to ensure BST validity.
        # Also track total nodes merged to ensure we used all trees.
        
        curr_trees_merged = 1
        n_trees = len(trees)
        
        # Helper to validate and merge
        min_limit = float('-inf')
        max_limit = float('inf')
        
        # We need a robust recursive function
        
        def traverse(node, min_v, max_v):
            nonlocal curr_trees_merged
            if not node: return True
            
            if not (min_v < node.val < max_v):
                return False
            
            # If leaf, try merge
            if not node.left and not node.right:
                if node.val in root_map and root_map[node.val] is not node:
                    # Merge
                    subtree = root_map[node.val]
                    node.left = subtree.left
                    node.right = subtree.right
                    curr_trees_merged += 1
                    # Remove from map prevents cycles or reuse?
                    del root_map[node.val] 
            
            if not traverse(node.left, min_v, node.val): return False
            if not traverse(node.right, node.val, max_v): return False
            return True
        
        # Important: Remove the super root from map so we don't merge it into itself (cycle)
        # Assuming unique values for roots
        if root.val in root_map:
             del root_map[root.val]

        if not traverse(root, min_limit, max_limit):
            return None
            
        if curr_trees_merged != n_trees:
            return None
            
        return root

if __name__ == "__main__":
    solution = Solution()
    # Mocking
    t1 = TreeNode(2, TreeNode(1))
    t2 = TreeNode(3, TreeNode(2), TreeNode(5))
    t3 = TreeNode(5, TreeNode(4))
    # Expected: t2 is root. 3 -> left(2->1), right(5->4)
    # Output: Valid tree
