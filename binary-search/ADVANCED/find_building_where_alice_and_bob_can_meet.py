# Find Building Where Alice and Bob Can Meet
# Problem: https://leetcode.com/problems/find-building-where-alice-and-bob-can_meet/
# (LC 2940)

from typing import List
import bisect

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        
        # Process queries
        # If alice at i, bob at j (assume i <= j).
        # If i == j, meet at i.
        # If heights[j] > heights[i], meet at j.
        # Otherwise, we need leftmost k > j such that heights[k] > heights[i] AND heights[k] > heights[j].
        # Since heights[k] must be > max(heights[i], heights[j]), and we know heights[i] >= heights[j] in the failing case?
        # Wait, if heights[j] <= heights[i], we need k > j with heights[k] > heights[i] (which implies > heights[j]).
        # So we look for leftmost k > j with heights[k] > val (val = max(h[i], h[j])).
        
        # Group queries by 'j' (the rightmost index).
        # We perform offline processing as we iterate through buildings.
        # At index `curr`, we want to answer pending queries that needed `k > j_old` with `heights[k] > val`.
        
        qs_by_r = [[] for _ in range(len(heights))]
        
        for q_idx, (a, b) in enumerate(queries):
            if a > b: a, b = b, a
            
            if a == b or heights[b] > heights[a]:
                ans[q_idx] = b
            else:
                # We need search in stored queries
                # We need specific conditions.
                # Just keeping (max_val, q_idx) at 'b' bucket is enough?
                # No, we need to find FIRST k > b such that heights[k] > heights[a].
                # We can store this requirement at `b`. When we iterate past `b`, we check.
                qs_by_r[b].append((heights[a], q_idx))
                
        # Monotonic Stack? No, we need to find leftmost.
        # We can maintain a data structure of pending queries (val, q_idx).
        # When we process building `k` with height H:
        # All pending queries with `val < H` are satisfied by `k`.
        # Since we want leftmost, we should process them immediately.
        # We can use a Min-Heap for pending queries?
        # Heap stores `(needed_height, q_idx)`.
        # If `heap.top().needed < current_H`, then `ans[q_idx] = k`, pop.
        
        import heapq
        min_heap = []
        
        for i, h in enumerate(heights):
            # 1. Process new queries starting at i
            # Actually queries are stored at `b`. "Start looking from b+1".
            # So queries in qs_by_r[i] are added to heap NOW.
            # But they cannot be satisfied by `i` itself?
            # Usually: "find leftmost building k > j".
            # If we are at `i`, and we have queries from `j=i`? 
            # They need k > i. So we add them to heap, to be satisfied by future buildings.
            # Wait, `qs_by_r` stores queries associated with `b`.
            # We add them to heap. They become candidates for i+1 onwards.
            # Can `i` satisfy queries from `qs_by_r[i]`? No, because we need k > b.
            # So `i` satisfies queries from `prev < i`.
            
            # Check if `i` satisfies older queries
            while min_heap and min_heap[0][0] < h:
                val, q_idx = heapq.heappop(min_heap)
                ans[q_idx] = i
                
            # Add new queries
            for needed_h, q_idx in qs_by_r[i]:
                heapq.heappush(min_heap, (needed_h, q_idx))
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.leftmostBuildingQueries([6,4,8,5,2,7], [[0,1],[0,3],[2,4],[3,4],[2,2]])) 
    # Output: [2,5,5,5,2]
