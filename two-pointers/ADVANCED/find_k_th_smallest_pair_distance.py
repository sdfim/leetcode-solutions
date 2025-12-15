# Find K-th Smallest Pair Distance
# Problem: https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# Solution:

from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def count_pairs(limit_dist):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > limit_dist:
                    left += 1
                count += right - left
            return count
            
        # Binary search for the answer
        low = 0
        high = nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= k:
                high = mid
            else:
                low = mid + 1
                
        return low

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,3,1]
    k1 = 1
    print(f"1st smallest pair distance in {nums1}: {solution.smallestDistancePair(nums1, k1)}")
    
    nums2 = [1,1,1]
    k2 = 2
    print(f"2nd smallest pair distance in {nums2}: {solution.smallestDistancePair(nums2, k2)}")
