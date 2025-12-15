# Russian Doll Envelopes
# Problem: https://leetcode.com/problems/russian-doll-envelopes/

from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by width ascending, then height descending
        # Why height desc? If widths equal, [3, 4] cannot contain [3, 3].
        # Sorting height desc ensures we don't pick multiple envelopes of same width
        # because the LIS logic would require strictly increasing subsequence of heights.
        # [3, 4], [3, 3] -> if we picked 4, we can't pick 3 (since seeking increasing).
        
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [x[1] for x in envelopes]
        
        # LIS on heights
        tails = []
        for h in heights:
            idx = bisect.bisect_left(tails, h)
            if idx < len(tails):
                tails[idx] = h
            else:
                tails.append(h)
                
        return len(tails)

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))  # Output: 3
