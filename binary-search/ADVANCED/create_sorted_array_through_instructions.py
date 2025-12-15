# Create Sorted Array through Instructions
# Problem: https://leetcode.com/problems/create-sorted-array-through-instructions/

from typing import List

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        m = max(instructions)
        tree = [0] * (m + 2)
        
        def update(i, delta):
            while i < len(tree):
                tree[i] += delta
                i += i & (-i)
                
        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s
            
        cost = 0
        for i, x in enumerate(instructions):
            # Strictly less: query(x - 1)
            less = query(x - 1)
            # Strictly greater: total_elements_so_far - query(x)
            # total elements = i
            greater = i - query(x)
            
            cost = (cost + min(less, greater)) % MOD
            update(x, 1)
            
        return cost

if __name__ == "__main__":
    solution = Solution()
    print(solution.createSortedArray([1,5,6,2])) # Output: 1
