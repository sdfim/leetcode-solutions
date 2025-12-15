# My Calendar II
# Problem: https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # Check if new booking overlaps with double bookings (overlaps list)
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        
        # Add overlaps to overlap list
        for s, e in self.calendar:
            if start < e and end > s:
                self.overlaps.append((max(start, s), min(end, e)))
        
        self.calendar.append((start, end))
        return True

if __name__ == "__main__":
    obj = MyCalendarTwo()
    print(obj.book(10, 20)) # True
    print(obj.book(50, 60)) # True
    print(obj.book(10, 40)) # True (Overlaps 10-20, OK)
    print(obj.book(5, 15))  # False (Overlaps 10-20 and 10-40 => Triple overlap at 10-15)
