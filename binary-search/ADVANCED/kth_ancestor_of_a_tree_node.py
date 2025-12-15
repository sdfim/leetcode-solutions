# Kth Ancestor of a Tree Node
# Problem: https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

from typing import List
import math

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.LOG = int(math.log2(n)) + 1
        self.up = [[-1] * self.LOG for _ in range(n)]
        
        for i in range(n):
            self.up[i][0] = parent[i]
            
        for j in range(1, self.LOG):
            for i in range(n):
                if self.up[i][j-1] != -1:
                    self.up[i][j] = self.up[self.up[i][j-1]][j-1]
                else:
                    self.up[i][j] = -1

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.LOG):
            if (k >> j) & 1:
                node = self.up[node][j]
                if node == -1:
                    return -1
        return node

if __name__ == "__main__":
    obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print(obj.getKthAncestor(3, 1)) # Output: 1
    print(obj.getKthAncestor(5, 2)) # Output: 0
    print(obj.getKthAncestor(6, 3)) # Output: -1
