# Determine if a Simple Graph Exists (Havel-Hakimi & Erdos-Gallai)
# Problem: https://leetcode.com/problems/determine-if-a-simple-graph-exists-from-degree-sequence/
# Note: This often appears as "Graph Realization" or checking degree sequences.

from typing import List
import bisect

class Solution:
    def isPossible(self, degrees: List[int]) -> bool:
        # Erdos-Gallai Theorem:
        # Sort d in descending order: d_1 >= ... >= d_n.
        # Sequence is graphic iff sum(d) is even AND for all k (1..n):
        # sum_{i=1}^k d_i <= k(k-1) + sum_{i=k+1}^n min(d_i, k)
        
        if sum(degrees) % 2 != 0:
            return False
            
        degrees.sort(reverse=True)
        n = len(degrees)
        
        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + degrees[i]
            
        # Check inequality for each k from 1 to n
        for k in range(1, n + 1):
            lhs = prefix[k]
            
            # Calculate rhs term: sum_{i=k+1}^n min(d_i, k)
            # Split index i > k into two parts:
            # 1. d_i >= k
            # 2. d_i < k
            # Since d is sorted descending, there's a split point.
            # Find largest index idx (>= k-1) such that d[idx] >= k.
            # Actually we search in range [k, n-1].
            
            # We want first index 'split' such that degrees[split] < k.
            # degs are: d_0, d_1 ... (0-indexed). d_{k-1} is k-th term.
            # We look at indices from k to n-1.
            
            # Degrees are reverse sorted.
            # To use bisect, we can use a negative list key or custom search.
            # Or manually binary search.
            
            # Find first index `split` in `degrees` (range k to n) where degrees[split] < k.
            # If all >= k, split = n.
            
            low, high = k, n
            split = n
            while low < high:
                mid = (low + high) // 2
                if degrees[mid] < k:
                    split = mid
                    high = mid
                else:
                    low = mid + 1
            
            # For indices from k to split-1: value is >= k. So min(d_i, k) = k.
            # Count = split - k. Sum = (split - k) * k.
            
            # For indices from split to n-1: value is < k. min(di, k) = di.
            # Sum = prefix[n] - prefix[split].
            
            term2 = (split - k) * k + (prefix[n] - prefix[split])
            rhs = k * (k - 1) + term2
            
            if lhs > rhs:
                return False
                
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPossible([3, 3, 3, 3])) # True (K4 minus 2 edges?)
    print(solution.isPossible([3, 2, 2, 1])) # True
    print(solution.isPossible([4, 3, 3, 3])) # False (Sum odd)
