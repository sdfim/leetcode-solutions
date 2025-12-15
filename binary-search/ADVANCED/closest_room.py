# Closest Room
# Problem: https://leetcode.com/problems/closest-room/

from typing import List
import bisect

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        # queries[i] = [preferred, minSize]
        # We need room with size >= minSize and abs(id - preferred) minimized.
        # If tie, smallest id.
        
        # Offline query processing.
        # Sort queries by minSize descending.
        # Sort rooms by size descending.
        
        # Add efficient structure to store IDs of available rooms.
        # We need something that supports insert and find_closest.
        # Python doesn't have a built-in SortedList (AVL/RedBlack).
        # But we can use `insort` on a list. Insertion is O(N), but total N insertions.
        # N=10^5, N^2 worst case. TLE likely if we use simple list.
        # However, for Python in competitive programming, manual SortedList or Coordinate Compression + Fenwick/Segment Tree is used.
        # Or simple array if test cases are weak? No, standard hard problem.
        
        # Since I can't import `sortedcontainers`, I need a workaround.
        # The IDs are static, but filtering by size changes availability.
        # Actually, we add rooms one by one.
        
        # Alternative: We can handle by segment tree over room IDs.
        # Maximize size in range? No, we filter by size first.
        # We process queries by size.
        # Add all valid rooms (size >= current_query_size) to a data structure.
        # Find closest ID in structure.
        
        # Hacky workaround for SortedList:
        # Since we only add elements, maybe we can use Segment Tree over the range of IDs [1, 10^7]?
        # IDs are up to 10^7. Sparse Segment Tree or Coordinate Compression.
        
        # Coordinate Compression of IDs:
        unique_ids = sorted(list(set(r[0] for r in rooms) | set(q[0] for q in queries)))
        id_map = {uid: i for i, uid in enumerate(unique_ids)}
        m = len(unique_ids)
        
        # Segment Tree to store strictly "indices that are active".
        # We want to find closest active index.
        # We can just store active indices in a list and binary search? No, inserting is slow.
        # But we can find predecessor and successor using Segment Tree.
        # Tree stores min_id and max_id in range?
        # Tree leaves track if ID is present. Node stores max_present_id in range.
        
        tree = [-1] * (4 * m)
        
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
            
        # Actually simpler: efficient finding of floor and ceil in BST.
        # Without SortedList, hard to do in Python cleanly.
        # I will implement a basic Segment Tree to querying "max id <= target" and "min id >= target".
        
        # Tree for Min
        min_tree = [float('inf')] * (4 * m)
        # Tree for Max
        max_tree = [float('-inf')] * (4 * m)
        
        def update_min(node, start, end, idx, val):
            if start == end:
                min_tree[node] = val
                return
            mid = (start + end) // 2
            if idx <= mid:
                update_min(2*node, start, mid, idx, val)
            else:
                update_min(2*node+1, mid + 1, end, idx, val)
            min_tree[node] = min(min_tree[2*node], min_tree[2*node+1])

        def query_min(node, start, end, l, r):
            if r < start or end < l:
                return float('inf')
            if l <= start and end <= r:
                return min_tree[node]
            mid = (start + end) // 2
            return min(query_min(2*node, start, mid, l, r),
                       query_min(2*node+1, mid + 1, end, l, r))
                       
        def update_max(node, start, end, idx, val):
            if start == end:
                max_tree[node] = val
                return
            mid = (start + end) // 2
            if idx <= mid:
                update_max(2*node, start, mid, idx, val)
            else:
                update_max(2*node+1, mid + 1, end, idx, val)
            max_tree[node] = max(max_tree[2*node], max_tree[2*node+1])

        def query_max(node, start, end, l, r):
            if r < start or end < l:
                return float('-inf')
            if l <= start and end <= r:
                return max_tree[node]
            mid = (start + end) // 2
            return max(query_max(2*node, start, mid, l, r),
                       query_max(2*node+1, mid + 1, end, l, r))

        # Attach original index to queries to restore order
        queries_with_index = []
        for i, q in enumerate(queries):
            queries_with_index.append((q[0], q[1], i))
            
        queries_with_index.sort(key=lambda x: x[1], reverse=True)
        rooms.sort(key=lambda x: x[1], reverse=True)
        
        ans = [-1] * len(queries)
        room_idx = 0
        n_rooms = len(rooms)
        
        for pref, min_size, q_idx in queries_with_index:
            while room_idx < n_rooms and rooms[room_idx][1] >= min_size:
                r_id = rooms[room_idx][0]
                mapped_idx = id_map[r_id]
                update_min(1, 0, m-1, mapped_idx, r_id)
                update_max(1, 0, m-1, mapped_idx, r_id)
                room_idx += 1
                
            if room_idx == 0:
                continue
            
            # Find largest id <= pref
            target_mapped = id_map[pref] # Approximate since pref might not be in query list? 
            # Wait, pref IS in query list, so it is in unique_ids.
            
            # Floor: search in range [0, target_mapped] for max value
            floor_val = query_max(1, 0, m-1, 0, target_mapped)
            
            # Ceil: search in range [target_mapped, m-1] for min value
            ceil_val = query_min(1, 0, m-1, target_mapped, m-1)
            
            res_id = -1
            min_dist = float('inf')
            
            if floor_val != float('-inf'):
                dist = abs(floor_val - pref)
                if dist < min_dist:
                    min_dist = dist
                    res_id = floor_val
                elif dist == min_dist:
                    res_id = min(res_id, floor_val)
                    
            if ceil_val != float('inf'):
                dist = abs(ceil_val - pref)
                if dist < min_dist:
                    min_dist = dist
                    res_id = ceil_val
                elif dist == min_dist:
                    res_id = min(res_id, ceil_val)
                    
            ans[q_idx] = res_id
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.closestRoom([[2,2],[1,2],[3,2]], [[3,1],[3,3],[5,2]]))
    # Output: [3, -1, 3]
