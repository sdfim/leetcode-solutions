#
# Problem: https://leetcode.com/problems/palindrome-partitioning/
# Solution:

from typing import List

def partition(s: str) -> List[List[str]]:
    # Palindrome Partitioning
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()

    def is_palindrome(sub):
        return sub == sub[::-1]

    result = []
    backtrack(0, [])
    return result


if __name__ == "__main__":
    s = "aab"
    print(partition(s))
