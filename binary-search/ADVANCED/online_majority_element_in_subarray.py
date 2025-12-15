# Online Majority Element In Subarray
# Problem: https://leetcode.com/problems/online-majority-element-in-subarray/

from typing import List
import collections
import random
import bisect

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.pos = collections.defaultdict(list)
        for i, x in enumerate(arr):
            self.pos[x].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        # Try random candidates 20 times
        for _ in range(20):
            idx = random.randint(left, right)
            candidate = self.arr[idx]
            
            # Check frequency of candidate in range [left, right]
            indices = self.pos[candidate]
            # First occurrence >= left
            l_idx = bisect.bisect_left(indices, left)
            # First occurrence > right (so indices up to this result are <= right)
            r_idx = bisect.bisect_right(indices, right)
            
            count = r_idx - l_idx
            if count >= threshold:
                return candidate
        return -1

if __name__ == "__main__":
    obj = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(obj.query(0, 5, 4)) # Output: 1
    print(obj.query(0, 3, 3)) # Output: -1
