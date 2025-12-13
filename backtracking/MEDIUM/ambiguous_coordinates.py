# Ambiguous Coordinates
# Problem: https://leetcode.com/problems/ambiguous-coordinates/
# Solution:

from typing import List

def ambiguousCoordinates(s: str) -> List[str]:
    def generate(s):
        n = len(s)
        for i in range(1, n + 1):
            left, right = s[:i], s[i:]
            if (len(left) > 1 and left[0] == "0" and left[1:] != "") or (len(right) > 0 and right[-1] == "0"):
                continue
            yield left + ("." + right if right else "")

    s = s[1:-1]
    result = []
    for i in range(1, len(s)):
        left, right = s[:i], s[i:]
        result.extend(f"({x}, {y})" for x in generate(left) for y in generate(right))
    return result

if __name__ == "__main__":
    s = "(123)"
    print(ambiguousCoordinates(s))
