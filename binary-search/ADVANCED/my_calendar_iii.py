# My Calendar III
# Problem: https://leetcode.com/problems/my-calendar-iii/

from typing import List
import bisect

class MyCalendarThree:

    def __init__(self):
        # Store points boundaries.
        # Alternatively use Segment Tree logic if range large?
        # N=400. N^2 is fine. 
        # Easier: Sweep line map.
        self.timeline = {}

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline[startTime] = self.timeline.get(startTime, 0) + 1
        self.timeline[endTime] = self.timeline.get(endTime, 0) - 1
        
        curr = 0
        ans = 0
        # Iterate sorted keys
        for t in sorted(self.timeline.keys()):
            curr += self.timeline[t]
            ans = max(ans, curr)
        return ans

if __name__ == "__main__":
    obj = MyCalendarThree()
    print(obj.book(10, 20)) # 1
    print(obj.book(50, 60)) # 1
    print(obj.book(10, 40)) # 2
    print(obj.book(5, 15))  # 3
    print(obj.book(5, 10))  # 3
    print(obj.book(25, 55)) # 3
