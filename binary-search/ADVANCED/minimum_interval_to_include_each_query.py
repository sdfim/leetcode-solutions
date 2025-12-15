# Minimum Interval to Include Each Query
# Problem: https://leetcode.com/problems/minimum-interval-to-include-each-query/
# (LC 1851)

from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by start time.
        # Sort queries (track indices).
        # Sweep line with Min-Heap storing (size, end).
        
        intervals.sort()
        qs = sorted([(q, i) for i, q in enumerate(queries)])
        
        ans = [-1] * len(queries)
        min_heap = [] # (size, end)
        
        idx = 0
        n_intervals = len(intervals)
        
        for q_val, q_idx in qs:
            # Add intervals starting <= q_val
            while idx < n_intervals and intervals[idx][0] <= q_val:
                s, e = intervals[idx]
                size = e - s + 1
                heapq.heappush(min_heap, (size, e))
                idx += 1
                
            # Remove intervals ending < q_val (can't cover q)
            while min_heap and min_heap[0][1] < q_val:
                heapq.heappop(min_heap)
                
            if min_heap:
                ans[q_idx] = min_heap[0][0]
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minInterval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5])) # [3,3,1,4]
