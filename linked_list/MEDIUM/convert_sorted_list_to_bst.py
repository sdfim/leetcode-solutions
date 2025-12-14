# Convert Sorted List to Binary Search Tree
# Problem: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Solution:

from typing import Optional
from linked_list.utils import ListNode, create_linked_list

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def find_middle(left, right):
            slow = fast = left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def convert_list_to_bst(left, right):
            if left == right:
                return None

            mid = find_middle(left, right)
            node = TreeNode(mid.val)

            node.left = convert_list_to_bst(left, mid)
            node.right = convert_list_to_bst(mid.next, right)
            return node

        return convert_list_to_bst(head, None)

if __name__ == "__main__":
    # Example use case
    linked_list = create_linked_list([-10, -3, 0, 5, 9])
    solution = Solution()
    bst = solution.sortedListToBST(linked_list)
    print("BST created from sorted linked list.")
