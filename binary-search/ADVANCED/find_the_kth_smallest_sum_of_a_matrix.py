# Find the Kth Smallest Sum of a Matrix With Sorted Rows
# Problem: https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

from typing import List

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        
        # Binary search for the sum
        left = 0
        right = 0
        for i in range(m):
            left += mat[i][0]
            right += mat[i][-1]
            
        initial_sum = left
        
        def count_sums(limit):
            # DFS to count how many combinations have sum <= limit
            # Optimization: 
            # If current sum exceeds limit, prune.
            # If we successfully count k+1, satisfy early.
            
            count = 0
            
            def dfs(row, current_sum):
                nonlocal count
                if count > k:
                    return
                
                if row == m:
                    count += 1
                    return
                
                for col in range(n):
                    if current_sum + mat[row][col] - mat[row][0] > limit: # Optimization bound logic
                        # Actually we pass 'remaining capacity' or sum.
                        # Since rows are sorted, if mat[row][col] makes it too big, indices > col will also be too big.
                        break
                    
                    # Estimate minimum possible remaining sum
                    # Lower bound for remaining rows is sum(mat[r][0] for r in row+1...m-1).
                    # Precomputing tail sums helps pruning.
                    
                    dfs(row + 1, current_sum + mat[row][col])
            
            # Revised DFS for correctness and simplicity
            # Pass 'limit'.
            # Need to subtract min possible sum of remaining rows to check feasibility?
            # Better: normalize the matrix?
            # Or just use the standard count with limit.
            
            # Trick: track count <= k.
            pass
            return count

        # Alternate logic:
        # Since k is small (<= 200), we can iterative merge rows.
        # Keep only k smallest sums after merging each row.
        
        current_sums = mat[0][:min(k, n)]
        
        for i in range(1, m):
            next_sums = []
            for s in current_sums:
                for val in mat[i]:
                    next_sums.append(s + val)
            next_sums.sort()
            current_sums = next_sums[:min(k, len(next_sums))]
            
        return current_sums[k-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.kthSmallest([[1,3,11],[2,4,6]], 5)) # Output: 7
