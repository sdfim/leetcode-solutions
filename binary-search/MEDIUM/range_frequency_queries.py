# Range Frequency Queries
# Problem: https://leetcode.com/problems/range-frequency-queries/

from typing import List
import collections
import bisect

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.indices = collections.defaultdict(list)
        for i, x in enumerate(arr):
            self.indices[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.indices:
            return 0
        arr = self.indices[value]
        # Count indices in [left, right]
        l = bisect.bisect_left(arr, left)
        r = bisect.bisect_right(arr, right)
        return r - l

if __name__ == "__main__":
    obj = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
    print(obj.query(1, 2, 4)) # 1
