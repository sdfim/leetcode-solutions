# Find Median from Data Stream
# Problem: https://leetcode.com/problems/find-median-from-data-stream/
# Solution:

import heapq

class MedianFinder:

    def __init__(self):
        # Two heaps:
        # small: max-heap (implemented as min-heap with negated values) stores the smaller half
        # large: min-heap stores the larger half
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(f"Median after 1, 2: {mf.findMedian()}")
    mf.addNum(3)
    print(f"Median after 1, 2, 3: {mf.findMedian()}")
