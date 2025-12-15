# Maximum Length of Repeated Subarray
# Problem: https://leetcode.com/problems/maximum-length-of-repeated-subarray/

from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Binary search on length
        def check(length):
            seen = set()
            for i in range(len(nums1) - length + 1):
                # Using tuple as hashable type. Rolling hash would be O(N)
                # Python slicing is expensive, makes it O(N*M) worst case inside check.
                # But typically efficient enough for medium constraints.
                seen.add(tuple(nums1[i : i + length]))
                
            for i in range(len(nums2) - length + 1):
                if tuple(nums2[i : i + length]) in seen:
                    return True
            return False
            
        left, right = 0, min(len(nums1), len(nums2))
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                left = 1
                continue
            if check(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.findLength([1,2,3,2,1], [3,2,1,4,7]))  # Output: 3
