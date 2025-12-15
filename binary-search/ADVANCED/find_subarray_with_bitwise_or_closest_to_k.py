# Find Subarray With Bitwise OR Closest to K
# Problem: https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # For each element, the number of distinct subarray ORs ending at this element is small (at most 30).
        # We can maintain the set of current OR values.
        
        current_ors = set()
        min_diff = float('inf')
        
        for num in nums:
            next_ors = {num}
            # Add num to all previous ORs
            for valid_or in current_ors:
                next_ors.add(valid_or | num)
            
            current_ors = next_ors
            
            for val in current_ors:
                min_diff = min(min_diff, abs(val - k))
                
        return min_diff

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDifference([1,2,4,5], 3)) # Output: 0
