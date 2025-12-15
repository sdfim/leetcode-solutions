# Find Right Interval
# Problem: https://leetcode.com/problems/find-right-interval/

from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Store start points with their original indices
        starts = sorted([(x[0], i) for i, x in enumerate(intervals)])
        start_points = [x[0] for x in starts]
        res = []
        
        for iv in intervals:
            end = iv[1]
            idx = bisect.bisect_left(start_points, end)
            if idx < len(starts):
                res.append(starts[idx][1])
            else:
                res.append(-1)
                
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.findRightInterval([[1,2]]))  # Output: [-1]
    print(solution.findRightInterval([[3,4],[2,3],[1,2]]))  # Output: [-1, 0, 1]
