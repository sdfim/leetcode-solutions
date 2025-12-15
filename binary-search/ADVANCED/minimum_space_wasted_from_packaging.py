# Minimum Space Wasted From Packaging
# Problem: https://leetcode.com/problems/minimum-space-wasted-from-packaging/

from typing import List
import bisect

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        n = len(packages)
        MOD = 10**9 + 7
        inf = float('inf')
        min_waste = inf
        
        sum_packages = sum(packages)
        
        for box in boxes:
            box.sort()
            # If the largest box is smaller than the largest package, we can't fit them all.
            if box[-1] < packages[-1]:
                continue
                
            current_waste = 0
            prev_idx = 0
            
            # Iterate through boxes, from small to large
            for b in box:
                # Find how many packages satisfy package <= b
                # We need index where package > b. bisect_right returns insertion point.
                idx = bisect.bisect_right(packages, b, lo=prev_idx)
                
                # Packages from prev_idx to idx - 1 are put into box b
                count = idx - prev_idx
                if count > 0:
                     # Waste = (b * count) - (sum of these packages)
                     # But we precomputed total sum, simpler:
                     # Total Space = sum(box_size * count_in_box)
                     # Total Waste = Total Space - Sum(Packages)
                     current_waste += b * count
                
                prev_idx = idx
                if prev_idx == n:
                    break
            
            min_waste = min(min_waste, current_waste)
            
        if min_waste == inf:
            return -1
            
        return (min_waste - sum_packages) % MOD

if __name__ == "__main__":
    solution = Solution()
    print(solution.minWastedSpace([2,3,5], [[4,8],[2,8]])) # Output: 6
