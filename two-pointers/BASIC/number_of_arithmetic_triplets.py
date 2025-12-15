# Number of Arithmetic Triplets
# Problem: https://leetcode.com/problems/number-of-arithmetic-triplets/
# Solution:

from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set(nums)
        count = 0
        
        for num in nums:
            if num + diff in seen and num + 2 * diff in seen:
                count += 1
                
        return count

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [0,1,4,6,7,10]
    diff1 = 3
    print(f"Arithmetic triplets in {nums1}, diff {diff1}: {solution.arithmeticTriplets(nums1, diff1)}")
