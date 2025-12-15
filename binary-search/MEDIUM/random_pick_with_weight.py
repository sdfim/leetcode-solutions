# Random Pick with Weight
# Problem: https://leetcode.com/problems/random-pick-with-weight/

from typing import List
import bisect
import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        curr = 0
        for weight in w:
            curr += weight
            self.prefix_sum.append(curr)
        self.total = curr

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        # Find first prefix_sum >= target
        idx = bisect.bisect_left(self.prefix_sum, target)
        return idx

if __name__ == "__main__":
    # Cannot deterministically test randomness, just run logic
    obj = Solution([1, 3])
    print(obj.pickIndex())
