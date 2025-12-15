# Time Based Key-Value Store
# Problem: https://leetcode.com/problems/time-based-key-value-store/

import collections
import bisect

class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
            
        values = self.store[key]
        # Binary search for the rightmost timestamp <= timestamp
        
        # We can use bisect.bisect_right
        # values is list of (time, val). Logic:
        # We need largest t_prev <= timestamp.
        # bisect_right with (timestamp, char_max) gives index i
        # items are sorted by timestamp. 
        # (timestamp, "{") is basically (timestamp, chr(123)), ensuring we get right boundary for equal timestamp
        
        i = bisect.bisect_right(values, (timestamp, "{"))
        
        if i == 0:
            return ""
        
        return values[i-1][1]

if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    print(obj.get("foo", 1))  # Output: "bar"
    print(obj.get("foo", 3))  # Output: "bar"
    obj.set("foo", "bar2", 4)
    print(obj.get("foo", 4))  # Output: "bar2"
    print(obj.get("foo", 5))  # Output: "bar2"
