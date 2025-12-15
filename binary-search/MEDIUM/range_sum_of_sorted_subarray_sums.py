# Range Sum of Sorted Subarray Sums
# Problem: https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subs = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                subs.append(s)
        
        subs.sort()
        mod = 10**9 + 7
        return sum(subs[left-1 : right]) % mod

if __name__ == "__main__":
    solution = Solution()
    print(solution.rangeSum([1,2,3,4], 4, 1, 5))  # Output: 13
