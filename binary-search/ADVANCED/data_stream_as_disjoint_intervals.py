# Data Stream as Disjoint Intervals
# Problem: https://leetcode.com/problems/data-stream-as-disjoint-intervals/

from typing import List
import bisect

class SummaryRanges:

    def __init__(self):
        # Store intervals as list of [start, end]
        # Keep sorted by start
        self.intervals = []

    def addNum(self, value: int) -> None:
        if not self.intervals:
            self.intervals.append([value, value])
            return
            
        # Check if exists (optimization step would be binary search check)
        # Using bisect to find position
        
        # Find position where value would be inserted based on start time
        idx = bisect.bisect_right(self.intervals, [value, float('inf')])
        
        # idx is the first interval with start > value.
        # So value relates to interval at idx-1 or idx.
        
        # Check overlap with previous interval
        if idx > 0:
            prev = self.intervals[idx-1]
            if prev[0] <= value <= prev[1]:
                return # Already present
            if prev[1] == value - 1:
                prev[1] = value
                # Check merge with next
                if idx < len(self.intervals) and self.intervals[idx][0] == value + 1:
                    prev[1] = self.intervals[idx][1]
                    self.intervals.pop(idx)
                return
                
        # Check overlap with next interval
        if idx < len(self.intervals):
            curr = self.intervals[idx]
            if curr[0] == value + 1:
                curr[0] = value
                # Check merge with previous? (Handled above if idx > 0)
                # If idx > 0, we checked prev. If we didn't merge with prev,
                # then prev[1] < value - 1. So no merge possible.
                return
                
        # No merge, insert new
        self.intervals.insert(idx, [value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

if __name__ == "__main__":
    obj = SummaryRanges()
    obj.addNum(1)
    obj.getIntervals()
    obj.addNum(3)
    obj.getIntervals()
    obj.addNum(7)
    obj.getIntervals()
    obj.addNum(2)
    print(obj.getIntervals()) # [[1,3], [7,7]]
    obj.addNum(6)
    print(obj.getIntervals()) # [[1,3], [6,7]]
