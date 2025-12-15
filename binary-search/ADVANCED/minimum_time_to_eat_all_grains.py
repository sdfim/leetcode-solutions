# Minimum Time to Eat All Grains
# Problem: https://leetcode.com/problems/minimum-time-to-eat-all-grains/

from typing import List

class Solution:
    def minimumTime(self, hens: List[int], grains: List[int]) -> int:
        hens.sort()
        grains.sort()
        
        def check(time):
            g_idx = 0
            for h in hens:
                if g_idx == len(grains):
                    break
                
                # Find the range of grains this hen can eat within 'time'
                # Hen at h. First grain at grains[g_idx].
                # Case 1: Grain is to the right (or at same pos). Cost = grain - h.
                # Case 2: Grain is to the left. Cost = h - grain.
                # If we pick a range [g_idx, end_idx], let left_most = grains[g_idx], right_most = grains[end_idx].
                
                # Logic: One hen covers a continuous segment of grains.
                # We greedily try to extend the segment for current hen as much as possible.
                
                start_grain = grains[g_idx]
                
                # Walk g_idx forward
                # Try to find max extending g_curr
                # Check condition for [start_grain ... current_grain] relative to h
                
                # Optimization using bisect is possible, but plain linear scan inside check matches hens/grains logic (O(N+M)).
                # Total complexity O((N+M) log Time).
                
                while g_idx < len(grains):
                    end_grain = grains[g_idx]
                    
                    # Calculate cost to visit start_grain and end_grain from h
                    # 1. h -> start -> end : dist = abs(h - start) + abs(end - start)
                    # 2. h -> end -> start : dist = abs(h - end) + abs(start - end)
                    # Minimal path is min(dist1, dist2) <= time
                    
                    d1 = abs(h - start_grain) + abs(end_grain - start_grain)
                    d2 = abs(h - end_grain) + abs(start_grain - end_grain)
                    
                    if min(d1, d2) <= time:
                        g_idx += 1
                    else:
                        break
            return g_idx == len(grains)

        left, right = 0, 2 * 10**9 # Roughly max pos diff * 2 ?
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumTime([3,6,7], [2,4,7,9])) # Output: 2
