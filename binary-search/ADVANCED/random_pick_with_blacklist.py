# Random Pick with Blacklist
# Problem: https://leetcode.com/problems/random-pick-with-blacklist/

from typing import List
import random

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        # We need to pick randomly from [0, n-1] excluding blacklist.
        # Total valid numbers: M = n - len(blacklist).
        # We can map the blacklist numbers in range [0, M-1] to some valid numbers in [M, n-1].
        
        self.b_len = len(blacklist)
        self.m = n - self.b_len
        self.mapping = {}
        
        # Blacklist items which are in range [0, M - 1] must be remapped.
        # Valid items in range [M, n - 1] can be used as targets.
        
        # 1. Identify which blacklist numbers are in [M, n - 1]. These block 'slots' but we don't pick them anyway.
        # 2. Identify which blacklist numbers are in [0, M - 1]. These need remapping.
        # 3. Identify valid numbers in [M, n - 1].
        
        last = n - 1
        b_set = set(blacklist)
        
        for b in blacklist:
            if b < self.m:
                # Need to find a valid remapping target starting from end
                while last in b_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self) -> int:
        r = random.randint(0, self.m - 1)
        if r in self.mapping:
            return self.mapping[r]
        return r

if __name__ == "__main__":
    obj = Solution(7, [2, 3, 5])
    print(obj.pick())
