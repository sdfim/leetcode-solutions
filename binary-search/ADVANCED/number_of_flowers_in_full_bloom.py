# Number of Flowers in Full Bloom
# Problem: https://leetcode.com/problems/number-of-flowers-in-full-bloom/

from typing import List
import bisect

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted([s for s, e in flowers])
        ends = sorted([e + 1 for s, e in flowers]) # Use e + 1 because bloom includes e
        
        res = []
        for p in people:
            # Number of flowers that have started blooming by time p
            # i = number of starts <= p
            started = bisect.bisect_right(starts, p)
            
            # Number of flowers that have finished blooming by time p (strictly before p, or at p?)
            # If flower ends at e, it stops blooming at e + 1.
            # So if e + 1 <= p, it is no longer blooming.
            finished = bisect.bisect_right(ends, p)
            
            res.append(started - finished)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]))
    # Output: [1,2,2,2]
