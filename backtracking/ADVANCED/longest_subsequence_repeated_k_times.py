# Longest Subsequence Repeated k Times
# Problem: https://leetcode.com/problems/longest-subsequence-repeated-k-times/
# Solution:

from typing import List
from collections import Counter

def longestSubsequenceRepeatedK(s: str, k: int) -> str:
    def is_valid(sub):
        count, i = 0, 0
        for char in s:
            if char == sub[i]:
                i += 1
                if i == len(sub):
                    count += 1
                    i = 0
            if count == k:
                return True
        return False

    def backtrack(path):
        nonlocal result
        if len(path) > len(result):
            if is_valid(path):
                result = path

        for char in freq:
            backtrack(path + char)

    freq = Counter(s)
    freq = [char for char, count in freq.items() if count >= k]
    result = ""
    backtrack("")
    return result

if __name__ == "__main__":
    s = "ababab"
    k = 2
    print(longestSubsequenceRepeatedK(s, k))
