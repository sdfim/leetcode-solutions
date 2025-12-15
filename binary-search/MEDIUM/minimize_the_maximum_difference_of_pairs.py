# Minimize the Maximum Difference of Pairs
# Problem: https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
# (LC 2616)

from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        
        def check(d):
            count = 0
            i = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= d:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p
            
        left, right = 0, nums[-1] - nums[0]
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimizeMax([10, 1, 2, 7, 1, 3], 2)) # 1
