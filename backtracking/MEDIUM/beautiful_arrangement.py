# Beautiful Arrangement
# Problem: https://leetcode.com/problems/beautiful-arrangement/
# Solution:

from typing import List

def countArrangement(n: int) -> int:
    def backtrack(index):
        if index > n:
            return 1
        count = 0
        for i in range(1, n + 1):
            if not used[i] and (index % i == 0 or i % index == 0):
                used[i] = True
                count += backtrack(index + 1)
                used[i] = False
        return count

    used = [False] * (n + 1)
    return backtrack(1)

if __name__ == "__main__":
    n = 2
    print(countArrangement(n))
