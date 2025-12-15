# Minimize Max Distance to Gas Station
# Problem: https://leetcode.com/problems/minimize-max-distance-to-gas-station/

from typing import List
import math

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        # We want to minimize D such that we can add k stations and make all gaps <= D.
        # For a gap G, we need ceil(G / D) - 1 stations to break it into pieces <= D.
        
        stations.sort()
        n = len(stations)
        
        def possible(D):
            count = 0
            for i in range(n - 1):
                gap = stations[i+1] - stations[i]
                if gap > D:
                    count += math.ceil(gap / D) - 1
            return count <= k
            
        left, right = 0, stations[-1] - stations[0]
        # precision requirements usually 10^-6
        while right - left > 1e-6:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return left

if __name__ == "__main__":
    solution = Solution()
    print(solution.minmaxGasDist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)) 
    # Output roughly 0.5
