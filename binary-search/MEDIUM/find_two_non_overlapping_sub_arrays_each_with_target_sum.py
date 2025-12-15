# Find Two Non-overlapping Sub-arrays Each With Target Sum
# Problem: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # 1. Find all subarrays with sum target. Store intervals [l, r].
        # 2. We need two non-overlapping [l1, r1], [l2, r2] such that len is minimized.
        
        # O(N) approach with hashmap for prefix sums
        prefix = {0: -1}
        acc = 0
        intervals = []
        
        for i, val in enumerate(arr):
            acc += val
            need = acc - target
            if need in prefix:
                start = prefix[need] + 1
                length = i - start + 1
                intervals.append((start, i, length))
            prefix[acc] = i
            
        # Now find two non-overlapping with min sum lengths
        # Sort intervals by end time? Or use DP/array.
        # min_len_ending_before[i] = min length of valid interval ending at or before i.
        
        n = len(arr)
        min_len_up_to = [float('inf')] * n
        min_l = float('inf')
        
        # We need to process strictly.
        # Re-process to build min_len_up_to properly.
        # Actually easier: iterate valid intervals.
        # Just use dynamic programming or track min_a.
        
        # Let's use a simpler pass:
        # min_len[i] stores min length of a valid subarray ending at or before index i.
        
        # Reset and do it cleanly
        
        min_len = [float('inf')] * n
        acc = 0
        prefix = {0: -1}
        cur_min = float('inf')
        ans = float('inf')
        
        for i, val in enumerate(arr):
            acc += val
            need = acc - target
            if need in prefix:
                prev_idx = prefix[need] # ended at prev_idx
                # subarray is from prev_idx + 1 to i
                curr_len = i - (prev_idx + 1) + 1
                
                # Check for non-overlapping solution
                # We need a solution ending at or before prev_idx
                if prev_idx >= 0 and min_len[prev_idx] != float('inf'):
                    ans = min(ans, curr_len + min_len[prev_idx])
                
                cur_min = min(cur_min, curr_len)
                
            min_len[i] = cur_min
            prefix[acc] = i
            
        return ans if ans != float('inf') else -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.minSumOfLengths([3,2,2,4,3], 3))  # Output: 2 ([3], [3])
    print(solution.minSumOfLengths([7,3,4,7], 7))    # Output: 2 ([7], [7])
