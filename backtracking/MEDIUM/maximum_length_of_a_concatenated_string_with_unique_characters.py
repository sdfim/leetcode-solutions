# Maximum Length of a Concatenated String with Unique Characters
# Problem: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# Solution:

from typing import List

def maxLength(arr: List[str]) -> int:
    def backtrack(index, current):
        if len(current) != len(set(current)):
            return 0
        if index == len(arr):
            return len(current)
        return max(backtrack(index + 1, current), backtrack(index + 1, current + arr[index]))

    return backtrack(0, "")

if __name__ == "__main__":
    arr = ["un", "iq", "ue"]
    print(maxLength(arr))
