# Reverse Pairs
# Problem: https://leetcode.com/problems/reverse-pairs/

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(start, end):
            if start >= end:
                return 0
            mid = (start + end) // 2
            cnt = merge_sort(start, mid) + merge_sort(mid + 1, end)
            
            # Count important reverse pairs
            j = mid + 1
            for i in range(start, mid + 1):
                # condition: nums[i] > 2 * nums[j]
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += (j - (mid + 1))
            
            # Merge
            nums[start:end+1] = sorted(nums[start:end+1])
            return cnt
            
        return merge_sort(0, len(nums) - 1)

if __name__ == "__main__":
    solution = Solution()
    print(solution.reversePairs([1,3,2,3,1]))  # Output: 2
    print(solution.reversePairs([2,4,3,5,1]))  # Output: 3
