# Flatten a Multilevel Doubly Linked List
# Problem: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Solution:

from typing import Optional

class Node:
    def __init__(self, val: int = 0, prev: 'Node' = None, next: 'Node' = None, child: 'Node' = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        def flatten_dfs(prev, curr):
            if not curr:
                return prev

            curr.prev = prev
            prev.next = curr

            temp_next = curr.next
            tail = flatten_dfs(curr, curr.child)
            curr.child = None
            return flatten_dfs(tail, temp_next)

        dummy = Node(0)
        flatten_dfs(dummy, head)
        dummy.next.prev = None
        return dummy.next

if __name__ == "__main__":
    # Example use case
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.prev = node1
    node2.child = node3
    solution = Solution()
    flattened_list = solution.flatten(node1)
    print("Multilevel doubly linked list flattened.")
