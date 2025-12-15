# Count Number of Rectangles Containing Each Point
# Problem: https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

from typing import List
import bisect
import collections

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # Rectangles have (l, h). 1 <= h <= 100.
        # Height is small!
        # Group rectangles by height.
        # rectangles[h] = sorted list of lengths 'l' for height 'h'.
        
        rects_by_h = collections.defaultdict(list)
        for l, h in rectangles:
            rects_by_h[h].append(l)
            
        for h in rects_by_h:
            rects_by_h[h].sort()
            
        ans = []
        for x, y in points:
            count = 0
            # A rectangle (l, h) contains (x, y) if l >= x and h >= y.
            # Iterate heights h from y to 100.
            for h in range(y, 101):
                if h in rects_by_h:
                    ls = rects_by_h[h]
                    # Count l >= x
                    idx = bisect.bisect_left(ls, x)
                    count += len(ls) - idx
            ans.append(count)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.countRectangles([[1,2],[2,3],[2,5]], [[2,1],[1,4]])) # [3, 1]
