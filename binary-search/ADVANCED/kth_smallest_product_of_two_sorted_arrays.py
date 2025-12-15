# Kth Smallest Product of Two Sorted Arrays
# Problem: https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

from typing import List
import bisect

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1, n2 = len(nums1), len(nums2)
        
        # We need to find number P such that count(product <= P) >= k.
        # Split arrays into positive and negative parts to handle sign logic easily.
        # Or handle with care in check function.
        
        def count_less_equal(val):
            count = 0
            for x in nums1:
                # We want x * y <= val
                if x > 0:
                    # y <= floor(val / x)
                    # Count element in nums2 <= val // x
                    # bisect_right returns count of elements <= limit (if duplicates, works)
                    limit = val // x
                    # Python // for negative results matches floor (e.g. -5 // 2 = -3). Correct.
                    count += bisect.bisect_right(nums2, limit)
                elif x < 0:
                    # y >= ceil(val / x)
                    # Because dividing by negative flips inequality
                    # y >= val / x
                    # Using floor division: y >= ceil(val/x).
                    # Python: val // x is floor. ceil is (val + x + 1) // x ? No.
                    # Correct ceil(a/b) where b < 0: (val + x + 1) // x if we want integer ceil? 
                    # Simpler: limit = ceil(val / x).
                    # We need count elements in nums2 >= limit.
                    # count = len(nums2) - bisect_left(nums2, limit).
                    import math
                    limit = math.ceil(val / x)
                    count += len(nums2) - bisect.bisect_left(nums2, limit)
                else: # x == 0
                    if val >= 0:
                        count += n2
            return count

        # Bounds
        min_p = min(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        max_p = max(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        
        # If arrays can contain 0, limits need care?
        # Absolute bounds are safely within signed 64-bit int.
        l, r = -10**10 - 7, 10**10 + 7 
        ans = l
        
        while l <= r:
            mid = (l + r) // 2
            if count_less_equal(mid) >= k:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.kthSmallestProduct([2,5], [3,4], 2)) # Output: 8
