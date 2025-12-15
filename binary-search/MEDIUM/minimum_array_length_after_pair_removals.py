# Minimum Array Length After Pair Removals
# Problem: https://leetcode.com/problems/minimum-array-length-after-pair-removals/

from typing import List
import collections

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        # Assuming sorted array nums.
        # Remove pairs (nums[i], nums[j]) such that nums[i] < nums[j].
        # Optimal strategy is to pair most frequent elements with others?
        # Actually, split array in half. Pair first half with second half.
        # Because it's sorted, nums[i] < nums[i + n/2] is likely?
        
        # But rigorous logic:
        # Max frequency element count 'max_f'.
        # If max_f > n/2, we are left with 2*max_f - n elements.
        # Else, we can remove everything (if n even) or 1 (if n odd).
        
        n = len(nums)
        # Find max freq
        # Since sorted, max freq is max run length? Not quite, just max count.
        # Actually counter is fine.
        
        counts = collections.Counter(nums)
        max_f = max(counts.values())
        
        if max_f > n / 2:
            return 2 * max_f - n
        
        return 1 if n % 2 else 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.minLengthAfterRemovals([1,2,3,4])) # 0
    print(solution.minLengthAfterRemovals([1,1,2,2,3,3])) # 0
    print(solution.minLengthAfterRemovals([1,1,1,2])) # 2 (4+ - 4 = 2)
