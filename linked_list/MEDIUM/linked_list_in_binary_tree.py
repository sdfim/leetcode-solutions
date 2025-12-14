# Linked List in Binary Tree
# Problem: https://leetcode.com/problems/linked-list-in-binary-tree/
# Solution:

from typing import Optional
from linked_list.utils import ListNode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node, head):
            if not head:
                return True
            if not node or node.val != head.val:
                return False
            return dfs(node.left, head.next) or dfs(node.right, head.next)

        if not root:
            return False
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

if __name__ == "__main__":
    # Example use case
    print("Check if linked list is a subpath in binary tree.")
