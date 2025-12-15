# Find a Value of a Mysterious Function Closest to Target
# Problem: https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        # Function func(arr, l, r) is bitwise AND of arr[l...r].
        # We want to minimize |func(arr, l, r) - target|.
        
        # Similar to OR, the set of AND values ending at index i is small (<= 30 distinct values).
        # We iteration through array and maintain possible AND values.
        
        valid_ands = set()
        ans = float('inf')
        
        for num in arr:
            new_ands = {num}
            for val in valid_ands:
                new_ands.add(val & num)
            valid_ands = new_ands
            
            for val in valid_ands:
                ans = min(ans, abs(val - target))
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.closestToTarget([9,12,3,7,15], 5)) # Output: 2
