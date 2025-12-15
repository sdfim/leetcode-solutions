# Find Weighted Median Node in Tree
# Problem: https://leetcode.com/problems/find-weighted-median-node-in-tree/
# (LC 3585 logic)

from typing import List
import math

class Solution:
    def medianNode(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Build adjacency
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        # Binary Lifting setup
        LOG = int(math.log2(n)) + 1
        up = [[-1] * LOG for _ in range(n)]
        depth_weighted = [0] * n
        depth_nodes = [0] * n # Number of edges from root
        
        # DFS
        stack = [(0, -1, 0, 0)] # node, parent, w_dist, node_dist
        
        while stack:
            u, p, d, nd = stack.pop()
            depth_weighted[u] = d
            depth_nodes[u] = nd
            up[u][0] = p
            
            for j in range(1, LOG):
                if up[u][j-1] != -1:
                    up[u][j] = up[up[u][j-1]][j-1]
                else:
                    up[u][j] = -1
                    
            for v, w in adj[u]:
                if v != p:
                    stack.append((v, u, d + w, nd + 1))
                    
        def get_lca(u, v):
            if depth_nodes[u] < depth_nodes[v]:
                u, v = v, u
            
            # Bring u to same node depth
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != -1 and depth_nodes[up[u][j]] >= depth_nodes[v]:
                    u = up[u][j]
                    
            if u == v: return u
            
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]

        def get_kth_ancestor(u, k_nodes):
            for j in range(LOG):
                if (k_nodes >> j) & 1:
                    u = up[u][j]
            return u
            
        # Find ancestor of u such that weighted distance from u is >= dist_req? 
        # Or close to dist_req?
        # We need first node x such that dist(u, x) >= limit.
        # Since we only have `up` pointers (jumps of 2^k *nodes*), we can't jump by weight easily unless weights are uniform.
        # But we can Binary Search on *node jumps*.
        # Path u->LCA has length (nodes) = depth_nodes[u] - depth_nodes[LCA].
        # We can binary search number of steps 's' up from u.
        # Check weighted dist: depth_weighted[u] - depth_weighted[kth_ancestor(u, s)].
        
        def find_node_at_weighted_dist_from_u_upwards(u, target_dist):
            # Find closest ancestor x such that dist(u, x) <= target_dist?
            # Or >=?
            # Problem: Weighted Median is first node where weight so far >= Total/2.
            # So find ancestor x with min distance >= Target. (Or max distance <= Target, then take next?)
            # Actually, walking up, distance increases. We want first x with dist >= target.
            
            # We can traverse bits of binary lifting from large to small?
            # If dist to (u + 2^j) < target, we move there and reduce target.
            # Standard "walk up" logic.
            curr = u
            current_dist = 0
            
            for j in range(LOG - 1, -1, -1):
                anc = up[curr][j]
                if anc != -1:
                    dist_jump = depth_weighted[curr] - depth_weighted[anc]
                    if current_dist + dist_jump < target_dist:
                        current_dist += dist_jump
                        curr = anc
            
            # Now curr is just below target. The parent of curr should satisfy >= target.
            # Unless curr itself satisfies?
            # Check:
            # If current_dist < target_dist, return up[curr][0].
            # Wait, if target_dist is 0, we return u.
            if target_dist <= 0: return u
            # The loop condition `current_dist + dist_jump < target_dist` ensures we stop BEFORE reaching/exceeding.
            # So `curr` is at distance < target.
            # `parent(curr)` is at distance >= target (or it's the target exact).
            return up[curr][0]

        res = []
        for u, v in queries:
            lca = get_lca(u, v)
            dist_u = depth_weighted[u] - depth_weighted[lca]
            dist_v = depth_weighted[v] - depth_weighted[lca]
            total_w = dist_u + dist_v
            
            # We want first node x such that dist(u, x) >= total_w / 2.
            limit = total_w / 2
            
            if limit <= dist_u:
                # Target is on u->LCA path
                # Find x on u->LCA such that dist(u, x) >= limit.
                # Use helper
                node = find_node_at_weighted_dist_from_u_upwards(u, limit)
                res.append(node)
            else:
                # Target is on LCA->v path
                # The distance from u is > dist_u.
                # Distance from v should be <= (total_w - limit)? No.
                # We need node x such that dist(u, x) >= limit.
                # dist(u, x) = dist_u + dist(lca, x).
                # So dist(lca, x) >= limit - dist_u.
                # dist(v, x) = dist_v - dist(lca, x).
                # So dist(v, x) <= dist_v - (limit - dist_u) = total_w - limit.
                # Since limit = total/2, total - limit is roughly total/2.
                # We need node x (closest to u) satisfying condition.
                # On LCA->v path, nodes further from v are closer to u.
                # We want node closest to u.
                # That corresponds to node furthest from v satisfying dist(v, x) <= total_w - limit?
                # No, wait.
                # dist(u, x) increases as we move u -> lca -> v.
                # We want FIRST node with val >= limit.
                # This node will have SMALLEST dist(u, x) >= limit.
                # Equivalent to LARGEST dist(v, x) <= dist_v - (limit - dist_u)?
                # No, dist(u, x) = Total - dist(v, x).
                # Total - dist(v, x) >= limit => dist(v, x) <= Total - limit.
                # We want SMALLEST dist(u, x) >= limit.
                # => LARGEST dist(v, x) <= Total - limit.
                
                # So we search upwards from v for ancestor x such that dist(v, x) <= Total - limit.
                # Actually helper `find_node_at_weighted_dist...` finds node with dist < Limit?
                # We loop while dist < Target.
                # We stop at `curr` with dist < Target.
                # We usually return parent which is >= Target.
                # Here we want the node ITSELF to be <= threshold.
                # So `curr` is exactly what we want?
                # Re-verify helper:
                # Helper finds parent of node with dist < T. i.e. First node >= T.
                # Here we want Last node (furthest from v) with dist(v, x) <= Threshold.
                # This corresponds to finding `curr` in the loop logic (largest dist < Threshold+epsilon).
                
                threshold = total_w - limit
                # Find x such that dist(v, x) <= threshold.
                # And we want x as far up as possible (closest to LCA).
                
                # Helper modification: Walk up while dist + jump <= threshold.
                curr = v
                current_dist = 0
                for j in range(LOG - 1, -1, -1):
                    anc = up[curr][j]
                    if anc != -1:
                        # Check we don't go above LCA
                        # Actually we can go up to LCA.
                        # We just need dist(v, anc) <= threshold.
                        # dist(v, anc) = depth_w[v] - depth_w[anc].
                        dist_jump = depth_weighted[curr] - depth_weighted[anc]
                        if current_dist + dist_jump <= threshold:
                            current_dist += dist_jump
                            curr = anc
                            
                # `curr` satisfies dist <= threshold.
                # Ancestor of `curr` would violate (dist > threshold).
                res.append(curr)
        
        return res

if __name__ == "__main__":
    solution = Solution()
    # Dummy
    print(solution.medianNode(3, [[0,1,1],[1,2,2]], [[0,2]])) # [1]
