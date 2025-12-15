# Count of Range Sum
# Problem: https://leetcode.com/problems/count-of-range-sum/

from typing import List
import bisect

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Prefix sums
        # We need lower <= prefix[j] - prefix[i] <= upper
        # prefix[j] - upper <= prefix[i] <= prefix[j] - lower
        
        # Merge Sort approach O(N log N) is standard for this.
        
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
            
        def merge_sort_count(lo, hi):
            if lo >= hi:
                return 0
            mid = (lo + hi) // 2
            count = merge_sort_count(lo, mid) + merge_sort_count(mid + 1, hi)
            
            # Count pairs across split
            # Using two pointers / cache
            j = k = mid + 1
            # Iterate left part
            for i in range(lo, mid + 1):
                # Find range in right part [mid+1...hi]
                # prefix[right] - prefix[left] >= lower => prefix[right] >= lower + prefix[left]
                while k <= hi and prefix[k] < lower + prefix[i]:
                    k += 1
                while j <= hi and prefix[j] <= upper + prefix[i]:
                    j += 1
                count += j - k
                
            # Merge step
            left_part = prefix[lo : mid + 1]
            right_part = prefix[mid + 1 : hi + 1]
            p1 = p2 = 0
            for p in range(lo, hi + 1):
                if p1 < len(left_part) and (p2 >= len(right_part) or left_part[p1] <= right_part[p2]):
                    prefix[p] = left_part[p1]
                    p1 += 1
                else:
                    prefix[p] = right_part[p2]
                    p2 += 1
            return count
            
        return merge_sort_count(0, len(prefix) - 1)

if __name__ == "__main__":
    solution = Solution()
    print(solution.countRangeSum([-2,5,-1], -2, 2))  # Output: 3
