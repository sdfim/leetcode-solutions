# Find K-th Smallest Pair Distance
# Problem: https://leetcode.com/problems/find-k-th-smallest-pair-distance/

from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        def count_pairs(limit):
            count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > limit:
                    left += 1
                count += right - left
            return count
            
        l, r = 0, nums[-1] - nums[0]
        res = 0
        
        while l <= r:
            mid = (l + r) // 2
            if count_pairs(mid) >= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestDistancePair([1,3,1], 1))  # Output: 0
