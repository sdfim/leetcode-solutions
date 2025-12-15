# Find the Longest Equal Subarray
# Problem: https://leetcode.com/problems/find-the-longest-equal-subarray/

from typing import List
import collections

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = collections.defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
            
        max_len = 0
        
        for x in pos:
            indices = pos[x]
            # Sliding window on indices
            # Window indices[l...r] represents a subarray from indices[l] to indices[r]
            # Containing (r - l + 1) occurrences of x.
            # Total length is indices[r] - indices[l] + 1.
            # Elements to delete = Total length - occurrences = (indices[r] - indices[l] + 1) - (r - l + 1).
            # We need deleted <= k.
            
            left = 0
            for right in range(len(indices)):
                while (indices[right] - indices[left] + 1) - (right - left + 1) > k:
                    left += 1
                max_len = max(max_len, right - left + 1)
                
        return max_len

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestEqualSubarray([1,3,2,3,1,3], 3)) # 3
