# Block Placement Queries
# Problem: https://leetcode.com/problems/block-placement-queries/

from typing import List
import bisect

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # We have an infinite number line, obstacles at 0 and potentially other points.
        # Query 1: [1, x] -> Place obstacle at x.
        # Query 2: [2, x, sz] -> Check if we can place a block of size `sz` in [0, x].
        # A block can be placed if there is a gap >= sz between obstacles in range [0, x].
        
        # We need to maintain obstacles and efficient range max query for gaps.
        # Since x can be up to 5 * 10^4, we can use a Segment Tree.
        # Max coordinate X = 50000.
        # Segment Tree stores: max gap in range.
        
        # But obstacles are points. Gaps are intervals between points.
        # SegTree over coordinates [0, max_x].
        # What value does leaf i store?
        # Maybe let's store "max gap ending at or before i"?
        # Actually, simpler: maintain sorted list of obstacles.
        # When we query [0, x], we look at all gaps fully within [0, x].
        # If we insert obstacles dynamically, standard gaps change.
        
        # Better approach: Segment Tree over the VALUES of coordinates?
        # Let's say we have obstacles at 0, 5, 10.
        # At index 5, we can store gap size (5 - 0) = 5.
        # At index 10, we can store gap size (10 - 5) = 5.
        # Query [0, x] means finding max value in SegTree for range [0, x].
        # Wait, if query is x=7, and we have gap 5 at index 5. We also need to check gap ending at x?
        # The partial gap after last obstacle before x: x - last_obstacle_before_x.
        
        # Algorithm:
        # 1. Store obstacles in a SortedList (or use bisect with list).
        # 2. Segment Tree on indices [0, 50000].
        #    Leaf `i` stores `i - prev_obstacle` if `i` is an obstacle, else 0?
        #    Yes. If obstacle at `p`, set tree[p] = p - (obstacle before p).
        #    BUT inserting an obstacle at `new` updates `new` AND the `next` obstacle.
        #    If sorted obstacles were ..., A, C, ... and we insert B between A and C.
        #    Update tree[C] = C - B.
        #    Update tree[B] = B - A.
        # 3. For Query 2 [x, sz]:
        #    max_gap = query_max(tree, 0, x)
        #    This covers all complete gaps ending <= x.
        #    Also check gap between `prev_obstacle_before_x` and `x`.
        #    This is `x - prev_obstacle`.
        #    Return max(max_gap, x - prev_obstacle) >= sz.
        
        # Since standard Python doesn't have SegmentTree or SortedList, we assume constraints allow O(N) or we implement SegTree.
        # X <= 5*10^4 is small. Operations <= 5*10^4.
        # SegTree is perfect.
        
        MAX_X = 50005
        tree = [0] * (4 * MAX_X)
        
        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = val
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2*node, start, mid, idx, val)
            else:
                update(2*node+1, mid + 1, end, idx, val)
            tree[node] = max(tree[2*node], tree[2*node+1])
            
        def query(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            return max(query(2*node, start, mid, l, r),
                       query(2*node+1, mid + 1, end, l, r))
                       
        obstacles = [0]
        # Initially, no other obstacles? Or assumes range starts empty? 
        # Usually problem starts with obstacles? "There is an obstruction at 0".
        
        ans = []
        import bisect
        
        for q in queries:
            type = q[0]
            if type == 1:
                x = q[1]
                # Find position
                idx = bisect.bisect_right(obstacles, x)
                obstacles.insert(idx, x)
                
                prev = obstacles[idx-1]
                # Update current x gap
                update(1, 0, MAX_X, x, x - prev)
                
                # Update next obstacle gap if exists
                if idx + 1 < len(obstacles):
                    next_obs = obstacles[idx+1]
                    update(1, 0, MAX_X, next_obs, next_obs - x)
                    
            else:
                x, sz = q[1], q[2]
                # Find largest complete gap ending <= x
                # Range query [0, x] on tree
                # Note: tree[i] is defined only at obstacle indices.
                # max valid gap ending <= x
                
                max_gap_complete = query(1, 0, MAX_X, 0, x)
                
                # Check residual gap ending at x
                # find obstacle <= x
                idx = bisect.bisect_right(obstacles, x)
                prev = obstacles[idx-1]
                gap_residual = x - prev
                
                if max(max_gap_complete, gap_residual) >= sz:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.getResults([[1,2],[2,3,3],[2,3,1],[2,2,2]])) 
    # Output: [False, True, True]
