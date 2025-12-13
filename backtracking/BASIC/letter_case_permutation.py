# Letter Case Permutation
# Problem: https://leetcode.com/problems/letter-case-permutation/
# Solution:

from typing import List

def letterCasePermutation(s: str) -> List[str]:
    def backtrack(index, path):
        if index == len(s):
            result.append("".join(path))
            return

        path.append(s[index])
        backtrack(index + 1, path)
        path.pop()

        if s[index].isalpha():
            path.append(s[index].swapcase())
            backtrack(index + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result

if __name__ == "__main__":
    s = "a1b2"
    print(letterCasePermutation(s))
