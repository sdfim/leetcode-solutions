# Snapshot Array
# Problem: https://leetcode.com/problems/snapshot-array/

from typing import List
import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        # List of lists. Each element is list of (snap_id, val)
        self.history = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.id, val))

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Find the value at snap_id. 
        # We need largest entry with id <= snap_id
        
        rec = self.history[index]
        i = bisect.bisect_right(rec, (snap_id, 10**9 + 7))
        return rec[i-1][1]

if __name__ == "__main__":
    obj = SnapshotArray(3)
    obj.set(0, 5)
    print(obj.snap())  # Output: 0
    obj.set(0, 6)
    print(obj.get(0, 0))  # Output: 5
