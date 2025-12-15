# Design Hit Counter
# Problem: https://leetcode.com/problems/design-hit-counter/

from typing import List
import bisect

class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # Return hits in range (timestamp - 300, timestamp]
        start_time = timestamp - 300
        
        # Binary search
        # bisect_right returns index where timestamp would be inserted.
        # Since we appended up to timestamp, all hits <= timestamp are in self.hits[:idx2]
        # We need > start_time.
        
        idx1 = bisect.bisect_right(self.hits, start_time)
        idx2 = bisect.bisect_right(self.hits, timestamp)
        
        return idx2 - idx1

if __name__ == "__main__":
    obj = HitCounter()
    obj.hit(1)
    obj.hit(2)
    obj.hit(3)
    print(obj.getHits(4))  # Output: 3
    obj.hit(300)
    print(obj.getHits(300)) # Output: 4
    print(obj.getHits(301)) # Output: 3
