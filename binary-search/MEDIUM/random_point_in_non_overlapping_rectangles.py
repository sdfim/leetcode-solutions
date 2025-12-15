# Random Point in Non-overlapping Rectangles
# Problem: https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

from typing import List
import random
import bisect

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix_areas = []
        curr = 0
        for x1, y1, x2, y2 in rects:
            # Number of points = (x2-x1+1) * (y2-y1+1)
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            curr += area
            self.prefix_areas.append(curr)
        self.total_points = curr

    def pick(self) -> List[int]:
        target = random.randint(1, self.total_points)
        idx = bisect.bisect_left(self.prefix_areas, target)
        
        rect = self.rects[idx]
        # Recover relative offset within this rectangle
        # Previous rects covered points up to self.prefix_areas[idx-1]
        base = self.prefix_areas[idx-1] if idx > 0 else 0
        offset = target - base - 1
        
        x1, y1, x2, y2 = rect
        width = x2 - x1 + 1
        height = y2 - y1 + 1
        
        # offset = row * width + col
        # row = offset // width, col = offset % width
        # But here coordinate system is typical
        
        x = x1 + (offset % width)
        y = y1 + (offset // width)
        
        return [x, y]

if __name__ == "__main__":
    obj = Solution([[-2,-2,-1,-1],[1,0,3,0]])
    print(obj.pick())
