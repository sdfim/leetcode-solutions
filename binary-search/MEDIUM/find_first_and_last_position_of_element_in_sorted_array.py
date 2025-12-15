# Find First and Last Position of Element in Sorted Array
# Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first):
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    res = mid
                    if is_first:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return res
            
        start = find_bound(True)
        if start == -1:
            return [-1, -1]
        end = find_bound(False)
        return [start, end]

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]
    print(solution.searchRange([5,7,7,8,8,10], 6))  # Output: [-1, -1]
