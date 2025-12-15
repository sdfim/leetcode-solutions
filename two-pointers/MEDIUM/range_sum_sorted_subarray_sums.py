# Range Sum of Sorted Subarray Sums
# Problem: https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
# Solution:

from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
                
        subarray_sums.sort()
        return sum(subarray_sums[left-1:right]) % (10**9 + 7)

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,2,3,4]
    n1 = 4
    left1 = 1
    right1 = 5
    print(f"Range sum {left1}-{right1} for {nums1}: {solution.rangeSum(nums1, n1, left1, right1)}")
