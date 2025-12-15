# Minimum Operations to Make a Subsequence
# Problem: https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

from typing import List
import bisect

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # target contains distinct integers.
        # We want to find the longest subsequence of arr that is a subsequence of target.
        # This is equivalent to finding LCS, but since target is distinct, we can reduce it to LIS.
        
        # Map each element in target to its index.
        val_to_idx = {val: i for i, val in enumerate(target)}
        
        # Transform arr into a list of indices.
        # Only include elements that are present in target.
        indices = []
        for x in arr:
            if x in val_to_idx:
                indices.append(val_to_idx[x])
                
        # Now find LIS of indices.
        # Use standard patience sorting / binary search algorithm for LIS.
        lis = []
        for idx in indices:
            pos = bisect.bisect_left(lis, idx)
            if pos == len(lis):
                lis.append(idx)
            else:
                lis[pos] = idx
                
        return len(target) - len(lis)

if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([5,1,3], [9,4,2,3,4])) # Output: 2
