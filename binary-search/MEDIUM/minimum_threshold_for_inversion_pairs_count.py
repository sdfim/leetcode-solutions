# Minimum Threshold for Inversion Pairs Count
# Problem: https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

from typing import List
import bisect

class Solution:
    def minThreshold(self, nums: List[int], k: int) -> int:
        
        # Binary search threshold X.
        # Check if count(inversions with limit X) >= k.
        
        def count_inversions(threshold):
            # Count pairs (i, j) i < j such that nums[i] > nums[j] and nums[i] - nums[j] <= threshold.
            
            # Use BIT or Merge Sort.
            # BIT approach: iterate j. Retrieve count of i < j such that:
            # nums[j] < nums[i] <= nums[j] + threshold.
            # Convert values to ranks.
            # Values can be large, use coordinate compression.
            # We need to query range (nums[j] + 1, nums[j] + threshold).
            
            temp_vals = set(nums)
            for x in nums:
                temp_vals.add(x + threshold) # We need to query up to here
                
            sorted_vals = sorted(temp_vals)
            rank_map = {v: i+1 for i, v in enumerate(sorted_vals)}
            m = len(sorted_vals)
            bit = [0] * (m + 1)
            
            def update(idx, val):
                while idx <= m:
                    bit[idx] += val
                    idx += idx & (-idx)
            
            def query(idx):
                s = 0
                while idx > 0:
                    s += bit[idx]
                    idx -= idx & (-idx)
                return s
            
            cnt = 0
            for x in nums:
                # Add x to BIT
                r = rank_map[x]
                update(r, 1)
                
                # Assume x is "nums[i]". (Wait, standard inversion order is usually reverse iteration or careful query)
                # Let's use standard direction: iterate j. BIT stores i's seen so far.
                # For current x = nums[j], we need count of stored i's such that:
                # nums[j] < nums[i] <= nums[j] + threshold.
                
                # Range [nums[j] + 1, nums[j] + threshold]
                low_val = x + 1
                high_val = x + threshold
                
                # Check boundaries
                # Actually rank_map might not have low_val/high_val exactly if we don't add them.
                # But we added (x + threshold).
                # Wait, "low_val" might be missing.
                pass 
                
            # Better approach:
            # Iterate j from 0 to n-1. BIT stores frequencies of nums[0...j-1].
            # Count i in BIT with val: (x, x + threshold].
            # Compression needs all possible query boundaries.
            
            # Re-collect values for compression
            all_vals = set(nums)
            # We will query ranges like [x+1, x+threshold].
            # Bisect is easier on sorted unique values if we map back to rank.
            # Or just use bisect.bisect on mapped values.
            
            # Since threshold is fixed in this check, compressed values are fixed? No, depend on threshold.
            # This makes compression needed inside check(threshold).
            # O(N log N) inside check. Total O(N log N log MaxVal). Acceptable.
            
            query_points = []
            for x in nums:
                query_points.append(x)
                query_points.append(x + threshold)
            query_points = sorted(list(set(query_points)))
            rank = {v: i+1 for i, v in enumerate(query_points)}
            max_rank = len(query_points)
            
            bit = [0] * (max_rank + 1)
            def bit_update(i, delta):
                while i <= max_rank:
                    bit[i] += delta
                    i += i & (-i)
            def bit_query(i):
                s = 0
                while i > 0:
                    s += bit[i]
                    i -= i & (-i)
                return s
                
            current_inversions = 0
            for x in nums:
                # x is nums[j]. Look for i < j (in BIT) such that x < nums[i] <= x + threshold.
                # Query range (rank[x], rank[x+threshold]] ? 
                # Range (x, x+threshold].
                # rank of x+threshold matches exactly or implies upper bound?
                # Keys in 'rank' cover x+threshold exactly.
                
                high_r = rank[x + threshold]
                low_r = rank[x] 
                
                # count = query(high_r) - query(low_r)
                # This gives elements in (x, x+threshold]. Correct.
                
                current_inversions += bit_query(high_r) - bit_query(low_r)
                
                bit_update(low_r, 1) # Add x to BIT
                
            return current_inversions

        # Binary Search
        
        # Min diff is 0? If nums[i] == nums[j]+0? No, nums[i] > nums[j] implies diff >= 1.
        # Threshold usually >= 1? Or 0 if strictly greater?
        # Condition: nums[i] - nums[j] <= x.
        # Since nums[i] > nums[j], diff is at least 1.
        # So x can be 1 to max_diff.
        # Return -1 if max inversions < k.
        
        # Check max possible inversions first?
        # Just check(infinity) call? Or sort-count.
        # Max inversions without threshold constraint is "all pairs i<j with nums[i]>nums[j]".
        # Basically count_inversions(infinity).
        # We can implement MergeSort to get max inversions quickly, but check() does it too if threshold is huge.
        
        max_diff = max(nums) - min(nums) if nums else 0
        left, right = 1, max_diff
        ans = -1
        
        # Optimization: verify total inversions first
        # But check function is fast enough.
        
        while left <= right:
            mid = (left + right) // 2
            if count_inversions(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minThreshold([1,2,3,4,3,2,1], 7)) # 2
