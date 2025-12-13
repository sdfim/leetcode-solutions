# Palindrome Permutation II
# Problem: https://leetcode.com/problems/palindrome-permutation-ii/
# Solution:

from typing import List
from collections import Counter

def generatePalindromes(s: str) -> List[str]:
    def backtrack(path):
        if len(path) == half_len:
            result.append("".join(path + mid + path[::-1]))
            return

        for char in counter:
            if counter[char] > 0:
                counter[char] -= 1
                path.append(char)
                backtrack(path)
                path.pop()
                counter[char] += 1

    counter = Counter(s)
    mid = [char for char, count in counter.items() if count % 2 == 1]
    if len(mid) > 1:
        return []

    mid = mid[0] if mid else ""
    half_len = len(s) // 2
    result = []
    backtrack([])
    return result

if __name__ == "__main__":
    s = "aabb"
    print(generatePalindromes(s))
