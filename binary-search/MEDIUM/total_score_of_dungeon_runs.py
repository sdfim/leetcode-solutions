# Total Score of Dungeon Runs
# Problem: https://leetcode.com/problems/total-score-of-dungeon-runs/

from typing import List

class Solution:
    def totalScore(self, n: int, initial_hp: int, damage: List[int], requirement: List[int]) -> int:
        # 1-based indexing in problem, 0-based implementation.
        # damage/req are length n. Indices 0 to n-1.
        
        # Condition: prefix_dmg[j-1] >= req[i] + prefix_dmg[i-1] - init_hp.
        # Or: prefix_dmg[j-1] >= C_i. For j <= i.
        
        # We iterate i from 0 to n-1.
        # C_i = req[i] + prefix_dmg[i-1] - init_hp.
        # We need to count j in [0, i] such that prefix_dmg[j-1] >= C_i.
        # Note: prefix_dmg[-1] = 0.
        
        prefix_dmg = [0] * (n + 1)
        curr = 0
        for idx in range(n):
            curr += damage[idx]
            prefix_dmg[idx+1] = curr # stored at +1 index
            
        # prefix_dmg array: [0, d0, d0+d1, ...]
        # j goes from 1 to i+1 (room indices).
        # j-1 corresponds to indices 0 to i in prefix_dmg.
        # Wait. J is starting room.
        # Loop i (current room). i goes from 0 to n-1.
        # Valid starts j are <= i + 1. (0 to i in 0-based).
        
        # We check condition for each i.
        # Count valid j <= i.
        # prefix_dmg[j] >= C_i where prefix_dmg[j] is sum of first j damages.
        # C_i calculation involves prefix_dmg[i] (sum of first i damages aka BEFORE i-th room).
        # Actually req[i] is requirement AFTER damage.
        # Wait, if room i is index k.
        # Damage D_k.
        # Health entering k: H. Exiting: H - D_k.
        # Condition: H - D_k >= R_k.
        # H = Init - (Sum damage from Start to k-1).
        # Init - (P[k] - P[Start]) - D_k >= R_k.
        # Init - P[k+1] + P[Start] >= R_k.
        # P[Start] >= P[k+1] - Init + R_k.
        
        # P[Start] is prefix sum up to start room.
        # Start ranges from 0 to k.
        # Values P[0], P[1]... P[k].
        # We query count of values in P[0...k] >= Threshold.
        
        # Use BIT or MergeSort Tree logic.
        # Since we query P[0...i] for each i, we can just add P[i] to BIT as we go.
        # Coordinate compression on P values + Thresholds.
        
        targets = []
        p_values = [0] * (n + 1)
        curr = 0
        p_values[0] = 0
        for k in range(n):
            curr += damage[k]
            p_values[k+1] = curr
            
            threshold = p_values[k+1] - initial_hp + requirement[k]
            targets.append(threshold)
            
        # Collect all values for rank map
        all_vals = set(p_values) | set(targets)
        sorted_vals = sorted(list(all_vals))
        rank = {v: i+1 for i, v in enumerate(sorted_vals)}
        m = len(sorted_vals)
        
        bit = [0] * (m + 1)
        def update(i, delta):
            while i <= m:
                bit[i] += delta
                i += i & (-i)
        def query(i): # sum 1..i
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
            
        ans = 0
        
        # Iterate rooms
        for k in range(n):
            # Check condition for room k (0-based)
            # Add valid starts for room k?
            # Actually valid start j <= k means we can start at 0..k.
            # So P[j] for j in 0..k are candidates.
            # P[k] is a candidate start (start at k, P[k] is sum before k).
            # So we add P[k] to BIT.
            
            r_val = rank[p_values[k]]
            update(r_val, 1)
            
            # Query count >= Threshold
            threshold = p_values[k+1] - initial_hp + requirement[k]
            r_thresh = rank[threshold]
            
            # Count elements >= r_thresh
            # Total elements so far is k+1.
            # Elements < r_thresh is query(r_thresh - 1).
            count = (k + 1) - query(r_thresh - 1)
            ans += count
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.totalScore(3, 10, [2,2,2], [5,5,5])) 
    # Room 0: req 5. Dmg 2. Exit 8. (8>=5 ok). Start 0 (init 10).
    # Room 1: req 5. Dmg 2. Exit 6. (6>=5 ok). Start 0.
    # Room 2: req 5. Dmg 2. Exit 4. (4<5 fail). Start 0.
    # Stars: 0->0(ok,sc1), 0->1(ok,sc1), 0->2(fail).
    # Start 1:
    # Room 1: Exit 8. (ok).
    # Room 2: Exit 6. (ok).
    # Start 2:
    # Room 2: Exit 8. (ok).
    # Total score = 1+1+0 + 1+1 + 1 = 5?
    # Logic: score is sum over all runs.
