# My Calendar I
# Problem: https://leetcode.com/problems/my-calendar-i/

import bisect

class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        # Find insertion point
        # Insert (start, end) if no overlap.
        # Check prev and next.
        
        # We can store as list of [s, e]
        # Sort by start.
        
        idx = bisect.bisect_left(self.calendar, (start, end))
        
        # Check previous event
        if idx > 0:
            prev_s, prev_e = self.calendar[idx - 1]
            if prev_e > start: # Overlap
                return False
                
        # Check next event
        if idx < len(self.calendar):
            next_s, next_e = self.calendar[idx]
            if next_s < end: # Overlap
                return False
                
        self.calendar.insert(idx, (start, end))
        return True

if __name__ == "__main__":
    obj = MyCalendar()
    print(obj.book(10, 20)) # True
    print(obj.book(15, 25)) # False
    print(obj.book(20, 30)) # True
