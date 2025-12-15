# Count the Number of Incremovable Subarrays II
# Problem: https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/

from typing import List
import bisect

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Find longest increasing prefix
        left_lim = 0
        while left_lim < n - 1 and nums[left_lim] < nums[left_lim + 1]:
            left_lim += 1
            
        if left_lim == n - 1:
            # Already sorted sorted, any subarray removal works (except empty removal? Problem says remove non-empty subarray)
            # Actually problem says "remove a subarray ... remaining array is strictly increasing".
            # Removing everything leaves empty, which is sorted.
            # Total subarrays: n*(n+1)/2.
            return n * (n + 1) // 2
            
        # Find longest increasing suffix
        right_lim = n - 1
        while right_lim > 0 and nums[right_lim - 1] < nums[right_lim]:
            right_lim -= 1
            
        # We need to remove subarray [i, j].
        # Remaining: prefix [0...i-1] and suffix [j+1...n-1].
        # Conditions:
        # 1. Prefix must be sorted -> i-1 <= left_lim
        # 2. Suffix must be sorted -> j+1 >= right_lim
        # 3. Connection: nums[i-1] < nums[j+1] (if both exist)
        
        count = 0
        
        # Case 1: Removing [0, j]. i=0. Left part empty (always sorted).
        # We need j+1 >= right_lim => j >= right_lim - 1.
        # Valid j in [right_lim - 1, n - 1].
        # Number of such j: n - 1 - (right_lim - 1) + 1 = n - right_lim + 1.
        # Actually simplest logic: iterate i from 0 to left_lim + 1.
        # i is the start of the removed subarray.
        # So we keep prefix nums[0...i-1]. (If i=0, prefix empty)
        # We need to find valid j >= i such that removing [i, j] works.
        # j must be such that suffix start (j+1) >= right_lim.
        # So j+1 can be max(right_lim, i+1? No j+1 > j >= i).
        # Also need nums[i-1] < nums[j+1].
        
        # Iterate i from 0 to left_lim + 1. (Length of prefix kept = i)
        # Prefix last element val = nums[i-1] if i>0 else -inf.
        # We need suffix starting at `k` such that `k >= right_lim` and `nums[k] > val`.
        # Smallest such `k`. Suffixes [k...n-1], [k+1...n-1]... are valid?
        # No, suffix [k...n-1] is fixed increasing.
        # If we pick start of suffix at `k`, we effectively remove [i, k-1].
        # We need to count valid `k`s.
        # For a fixed `i`, any `k >= right_lim` such that `nums[k] > nums[i-1]` is valid.
        # Number of such `k`s = number of valid removal end points.
        # Wait, removing [i, k-1] corresponds to picking suffix start `k`.
        # `k` can range from `max(right_lim, i+1)` to `n`. (k=n means removing everything till end).
        
        ans = 0
        # Valid suffix start indices: [right_lim, n]. element at n is effectively inf?
        # Let's consider indices in `nums` [right_lim, right_lim+1 ... n-1].
        # nums[n] is effectively infinity.
        
        suffix_starts = nums[right_lim:] 
        # But we need original indices or just count? Just count.
        # suffix_starts is sorted restricted to [right_lim...n-1].
        
        for i in range(left_lim + 2): # i is number of elements kept in prefix. 0 to left_lim+1.
            # Prefix: nums[0...i-1].
            # Last element:
            if i == 0:
                last_val = float('-inf')
            else:
                last_val = nums[i-1]
                
            # Find smallest index `k` in suffix part (>= right_lim) such that nums[k] > last_val.
            # Using bisect on the sorted suffix part.
            # We treat the suffix part as array `nums[right_lim:]`.
            # Find insertion point.
            
            idx_in_suffix = bisect.bisect_right(nums, last_val, lo=right_lim) 
            # bisect_right: items > last_val start from idx_in_suffix.
            # Valid k's are idx_in_suffix, idx_in_suffix+1 ... n-1.
            # PLUS the case where we remove everything up to end (k=n)?
            # Yes, if we remove [i...n-1], remaining is just prefix, which is valid.
            # "k=n" corresponds to suffix being empty.
            # Empty suffix is valid (sorted).
            # So valid k range is [idx_in_suffix, n].
            # Count = n - idx_in_suffix + 1.
            
            ans += (n - idx_in_suffix + 1)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.incremovableSubarrayCount([1,2,3,4])) # Output: 10
