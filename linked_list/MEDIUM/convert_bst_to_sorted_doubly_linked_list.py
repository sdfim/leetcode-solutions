# Convert Binary Search Tree to Sorted Doubly Linked List
# Problem: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# Solution:

from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        def inorder(node):
            nonlocal first, last
            if not node:
                return
            inorder(node.left)
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            inorder(node.right)

        first, last = None, None
        inorder(root)
        last.right = first
        first.left = last
        return first


if __name__ == "__main__":
    # Example use case
    root = Node(4, Node(2, Node(1), Node(3)), Node(5))
    solution = Solution()
    doubly_linked_list = solution.treeToDoublyList(root)
    print("BST converted to sorted doubly linked list.")
