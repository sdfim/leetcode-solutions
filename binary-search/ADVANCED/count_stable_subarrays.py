# Count Stable Subarrays
# Problem: https://leetcode.com/problems/count-stable-subarrays/
# (Assuming LC 3748 / Recent Contest definition)

from typing import List

class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Stable subarray: non-decreasing.
        # Queries ask for number of stable subarrays fully contained in [l, r].
        
        # 1. Identify valid stable segments.
        # e.g. [1, 2, 3, 1, 2] -> Segments: [1, 2, 3] (idxs 0-2), [1, 2] (idxs 3-4).
        # A subarray is stable iff it is contained within one of these maximal stable segments.
        
        n = len(nums)
        # Calculate max stable segment end for each start
        # Or faster: find boundaries where nums[i] > nums[i+1].
        # These are "breaks".
        
        breaks = [i for i in range(n - 1) if nums[i] > nums[i+1]]
        # A range [start, end] is stable if it contains NO breaks.
        # intersection of [start, end] with breaks is empty.
        
        # This means given [L, R], we want to count pairs (i, j) such that L <= i <= j <= R and no break in [i, j-1].
        # Equivalently, for each i in [L, R], let next_break[i] be the first break >= i.
        # The max j for this i is bounded by next_break[i] (actually break at k means k and k+1 are inverted, so subarray can go up to k).
        # Actually max j is min(R, boundary_of_segment(i)).
        
        # Let 'boundary[i]' be the rightmost index reachable from i in a stable subarray.
        # Then for query [L, R], we sum (min(boundary[i], R) - i + 1) for i in L..R.
        # = sum(min(boundary[i], R)) - sum(i) + (R - L + 1)
        # = sum(min(boundary[i], R)) - (L+R)*(R-L+1)/2 + (R-L+1)
        
        # Key term: sum_{i=L}^{R} min(boundary[i], R)
        # boundary[i] is a step function. It is constant within each maximal stable segment.
        # e.g. if segment is [s, e], then for k in s..e, boundary[k] = e.
        
        # Since queries are offline (or we can use online), we need to query sum of min(vals, const).
        # We can use binary search to find split point given simple structure of 'boundary'.
        # 'boundary' array is non-decreasing! 
        # Actually boundary[i] is the end of the run containing i.
        # If runs are [0, 2], [3, 4], ...
        # i=0 -> 2, i=1 -> 2, i=2 -> 2. i=3 -> 4, i=4 -> 4.
        # It is non-decreasing.
        
        # We want sum_{i=L}^{R} min(boundary[i], R).
        # Find split point where boundary[i] > R.
        # Since boundary is monotonic, use bisect.
        
        # Construct boundary array
        boundary = [0] * n
        curr_start = 0
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                # End of run at i
                for k in range(curr_start, i + 1):
                    boundary[k] = i
                curr_start = i + 1
        for k in range(curr_start, n):
            boundary[k] = n - 1
            
        # Prefix sum of boundary for range sum query
        prefix_boundary = [0] * (n + 1)
        for i in range(n):
            prefix_boundary[i+1] = prefix_boundary[i] + boundary[i]
            
        import bisect
        
        res = []
        for l, r in queries:
            # We want sum_{i=l}^{r} min(boundary[i], r)
            # Find first index k in [l, r] such that boundary[k] >= r.
            # Since boundary is increasing, we can search in [l, r].
            # Actually boundary[k] might jump. But it's monotonic.
            
            # bisect_left on boundary array for value `r` ?
            # boundary[k] >= r.
            # search range [l, r]
            
            # k = minimal index >= l such that boundary[k] >= r
            # Since we look in [l, r], if boundary[l] >= r, then all are >= r (capped at r).
            # If boundary[r] < r (impossible since boundary[r] >= r always), etc.
            
            # Using bisect on the full boundary array is fine, then clamp result to [l, r].
            
            k_idx = bisect.bisect_left(boundary, r, lo=l, hi=r+1)
            
            # For i in [l, k_idx - 1]: boundary[i] < r. Contribution is sum(boundary[i]).
            # For i in [k_idx, r]: boundary[i] >= r. Contribution is r.
            
            sum_portion = 0
            if k_idx > l:
                sum_portion = prefix_boundary[k_idx] - prefix_boundary[l]
            
            capped_portion = 0
            if k_idx <= r:
                capped_portion = (r - k_idx + 1) * r
                
            term1 = sum_portion + capped_portion
            
            # Formula: sum(min...) - sum(i) + (R-L+1)
            # sum(i) for i in l..r = (l+r)*(r-l+1)//2
            term2 = (l + r) * (r - l + 1) // 2
            
            ans = term1 - term2 + (r - l + 1)
            res.append(ans)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.countStableSubarrays([3,1,2], [[0,1],[1,2]])) # Output: [2, 3]
