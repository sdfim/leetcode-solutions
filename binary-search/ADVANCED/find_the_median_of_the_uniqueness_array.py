# Find the Median of the Uniqueness Array
# Problem: https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

from typing import List
import collections

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        total_subarrays = n * (n + 1) // 2
        median_idx = (total_subarrays + 1) // 2
        
        def count_subarrays_with_distinct_at_most(k):
            count = 0
            start = 0
            freq = collections.defaultdict(int)
            distinct_count = 0
            
            for end in range(n):
                if freq[nums[end]] == 0:
                    distinct_count += 1
                freq[nums[end]] += 1
                
                while distinct_count > k:
                    freq[nums[start]] -= 1
                    if freq[nums[start]] == 0:
                        distinct_count -= 1
                    start += 1
                
                count += (end - start + 1)
            return count

        # Binary search for median value of distinct counts
        # Range [1, count of distinct in full array] or [1, N]
        left, right = 1, len(set(nums))
        ans = 1
        
        while left <= right:
            mid = (left + right) // 2
            if count_subarrays_with_distinct_at_most(mid) >= median_idx:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.medianOfUniquenessArray([1,2,3])) # Output: 1
