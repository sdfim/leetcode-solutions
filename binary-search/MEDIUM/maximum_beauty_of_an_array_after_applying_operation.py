# Maximum Beauty of an Array After Applying Operation
# Problem: https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        # Find longest subsequence such that for all x in sub, ranges [x-k, x+k] overlap.
        # This means max(sub) - k <= min(sub) + k => max(sub) - min(sub) <= 2*k.
        # Since sorted, find longest subarray with nums[j] - nums[i] <= 2*k.
        
        limit = 2 * k
        l = 0
        ans = 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > limit:
                l += 1
            ans = max(ans, r - l + 1)
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumBeauty([4,6,1,2], 2)) # 3
