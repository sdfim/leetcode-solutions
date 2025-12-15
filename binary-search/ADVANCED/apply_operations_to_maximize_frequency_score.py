# Apply Operations to Maximize Frequency Score
# Problem: https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

from typing import List

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
            
        # We want to find largest window size L such that we can make all elements in window equal to median with cost <= k.
        
        def calculate_cost(l, r):
            # Window nums[l...r]
            # Median index
            mid = (l + r) // 2
            median = nums[mid]
            
            # Cost = (median * count_left - sum_left) + (sum_right - median * count_right)
            # Left part: [l, mid] (inclusive? median is at mid)
            # Actually cost is sum(abs(x - median))
            
            # Left side [l, mid]: sum is prefix[mid+1] - prefix[l]
            # elements are <= median. So cost += median * (mid - l + 1) - (prefix[mid+1] - prefix[l])
            
            # Right side [mid+1, r]: sum is prefix[r+1] - prefix[mid+1]
            # elements are >= median. cost += (prefix[r+1] - prefix[mid+1]) - median * (r - mid)
            
            cost = 0
            
            # Left part [l, mid]
            cnt_l = mid - l + 1
            sum_l = prefix[mid+1] - prefix[l]
            cost += median * cnt_l - sum_l
            
            # Right part [mid+1, r]
            cnt_r = r - mid # (r+1) - (mid+1)
            sum_r = prefix[r+1] - prefix[mid+1]
            cost += sum_r - median * cnt_r
            
            return cost
            
        max_freq = 0
        left = 0
        for right in range(n):
            while calculate_cost(left, right) > k:
                left += 1
            max_freq = max(max_freq, right - left + 1)
            
        return max_freq

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxFrequencyScore([1,2,6,4], 3)) # Output: 3
