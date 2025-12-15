# Maximum Average Subarray II
# Problem: https://leetcode.com/problems/maximum-average-subarray-ii/

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Binary search on Average
        min_val, max_val = min(nums), max(nums)
        
        error = 1e-5
        
        def check(avg):
            # Check if there is a subarray with length >= k having average >= avg
            # sum(nums[i...j]) / (j-i+1) >= avg
            # sum(nums[i...j] - avg) >= 0
            
            # Use prefix sums of (nums[i] - avg)
            curr = 0
            prev_min = 0
            # We need to maintain sum up to i - k
            # Actually easier: maintain cumulative sum.
            
            # Transform nums: arr[i] = nums[i] - avg
            # Check if exists subarray sum >= 0 with length >= k
            
            prefix = [0.0] * (len(nums) + 1)
            for i in range(len(nums)):
                prefix[i+1] = prefix[i] + (nums[i] - avg)
                
            min_pre = 0.0
            for i in range(k, len(nums) + 1):
                if prefix[i] - min_pre >= 0:
                    return True
                min_pre = min(min_pre, prefix[i - k + 1])
                
            return False
            
        while max_val - min_val > error:
            mid = (min_val + max_val) / 2
            if check(mid):
                min_val = mid
            else:
                max_val = mid
                
        return max_val

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))  # Output: 12.75
