# Maximum Frequency of an Element After Performing Operations I
# Problem: https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/
# (Assuming LC 3004 / 3346 logic)

from typing import List
import collections

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # IMPORTANT: This might be LC 3346.
        # We can change nums[i] to value in [nums[i]-k, nums[i]+k].
        # We want to maximize freq of some target value. At most numOperations changes.
        
        # Events based sweep line.
        # For each x=nums[i], it can become any value in [x-k, x+k].
        # So x contributes to range [x-k, x+k].
        # We want a point Y covered by max ranges, constrained by numOperations.
        # Actually, if we pick target Y, we can convert x to Y if |x-Y| <= k.
        # So we want Y such that count(x with |x-Y|<=k) is max, but we can only change numOps.
        # Wait, if x is already Y, it doesn't cost an operation.
        # Cost is 1 if x!=Y, 0 if x==Y.
        # Maximize: count(x == Y) + min(count(x != Y s.t. |x-Y|<=k), numOperations).
        # = min(count(x s.t. |x-Y|<=k), count(x==Y) + numOperations).
        
        # The interesting Y values are around nums[i], nums[i]-k, nums[i]+k etc.
        # Sweep line approach.
        # Intervals: [nums[i]-k, nums[i]+k].
        # Points: nums[i] (exact matches).
        
        # We process coordinates.
        # Use a dictionary or sorted events.
        
        events = []
        for x in nums:
            events.append((x - k, 1))
            events.append((x + k + 1, -1))
            events.append((x, 0)) # To ensure we check x exactly
            
        events.sort()
        
        count_in_range = 0
        ans = 0
        freq_map = collections.Counter(nums)
        
        for val, type_ in events:
            # type_ 1: start range, -1: end range, 0: exact check
            # BUT we need to handle multiple events at same coordinate carefully.
            # Especially x and x in range.
            pass
            
        # Refined sweep line:
        # Collect all boundary points.
        points = set()
        for x in nums:
            points.add(x)
            points.add(x - k)
            points.add(x + k + 1) # actually we want to check ranges
            
        # Actually, simpler: merge intervals?
        # Just use sorted nums?
        # For a target Y, candidates are nums[i] or boundary.
        # Efficient approach: sliding window on sorted nums?
        # If we target Y, we want nums in [Y-k, Y+k].
        # Size of window is defined by values range.
        
        nums.sort()
        # Max Y such that count within [Y-k, Y+k] is maximized?
        # Window size is 2*k.
        # Find max elements in range of size 2*k.
        # Let's say window includes nums[l...r]. Range [nums[l], nums[l] + 2k].
        # If we pick target Y = (nums[l] + nums[r])/2 ?
        # Actually, for a fixed window of indices l..r, can we align them to some Y?
        # Yes if nums[r] - nums[l] <= 2*k.
        # Then we can pick Y such that [Y-k, Y+k] covers [nums[l], nums[r]].
        # e.g. Y = nums[l] + k. Then [nums[l], nums[l]+2k] covers nums[l]..nums[r].
        
        # So we slide window over nums.
        # Maintain window such that nums[r] - nums[l] <= 2*k.
        # Elements in window can all be converted to Y = nums[l] + k (or similar).
        # Count is r - l + 1.
        # But limited by: count(x==Y) + numOperations.
        # This is tricky because Y is not fixed in the sliding window logic (Y varies continuously).
        # But the bound "count(x==Y) + numOperations" depends on Y being exactly a value in nums?
        # No, Y can be anything.
        # But if Y is not in nums, count(x==Y) is 0. So we are capped at numOperations.
        # If Y is in nums, cap is freq[Y] + numOperations.
        
        # So max freq is:
        # Method A: Y matches one of the numbers in nums.
        #   For each unique val in nums:
        #   Y = val.
        #   Count neighbors in [val-k, val+k].
        #   Total = count.
        #   Realizable = min(Total, freq[val] + numOperations).
        
        # Method B: Y is not one of the numbers (or doesn't matter).
        #   We just align `numOperations` elements to Y.
        #   Max possible is `numOperations`. (If no exact matches).
        #   Actually, if we have a window of size `M`, and NO elements are exactly Y, we can convert M elements to Y IF M <= numOperations.
        #   So if we pick Y not in nums, answer is bounded by numOperations.
        #   Wait, if we can convert M elements, ans is M.
        #   So simply: max_elements_in_range_2k.
        #   Let MaxRangeVal = max elements fitting in interval of len 2k.
        #   Answer is min(MaxRangeVal, numOperations)?
        #   No. If MaxRangeVal > numOperations, we can only convert numOperations.
        #   So we get at most numOperations.
        
        # Combining:
        # 1. Start with global max = `numOperations` (achievable by picking Y far from any points but hitting numOperations points? No, if we pick Y, we convert available points).
        # Actually, global max is at least `min(max_window_size, numOperations)`.
        
        # 2. Check specific Y = nums[i].
        # For each unique x in nums:
        #   window [x-k, x+k].
        #   Get count of nums in this window.
        #   ans = max(ans, min(count, freq[x] + numOperations)).
        
        # This covers all cases because if optimal Y is not in nums, its contribution from "exact match x==Y" is 0, so limited by numOperations.
        # And any window of length 2k contains some count. Max possible from strictly conversions is numOperations.
        # Unless checks at unique x yield higher.
        
        # Implementation:
        # 1. Calc max window size for range 2*k. -> `max_w`.
        #   Is result always limited by `max_w`? No.
        #   Actually result is `min(max_w, numOperations)` IF we use non-existing Y.
        #   But maybe checking `unique x` is sufficient.
        
        # Let's refine.
        # Ans = 0.
        # For distinct x in nums:
        #   C = count in [x-k, x+k].
        #   Ans = max(Ans, min(C, freq[x] + numOperations))
        # AND check generic case:
        #   Max window size W covering range 2k.
        #   Ans = max(Ans, min(W, numOperations))
        
        # Complexity: Sort O(N log N). Sliding window O(N).
        
        nums.sort()
        freq = collections.Counter(nums)
        unique_nums = sorted(freq.keys())
        
        ans = 0
        left = 0
        n = len(nums)
        
        # Generic check
        for right in range(n):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            w = right - left + 1
            ans = max(ans, min(w, numOperations))
            
        # Specific check for Y in unique_nums
        # Binary search range [x-k, x+k]
        import bisect
        for x in unique_nums:
            l_idx = bisect.bisect_left(nums, x - k)
            r_idx = bisect.bisect_right(nums, x + k)
            count = r_idx - l_idx
            
            can_achieve = min(count, freq[x] + numOperations)
            ans = max(ans, can_achieve)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxFrequency([1,4,5], 1, 2)) # 2
