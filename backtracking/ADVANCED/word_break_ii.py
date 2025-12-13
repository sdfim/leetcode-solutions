# Word Break II
# Problem: https://leetcode.com/problems/word-break-ii/
# Solution:

from typing import List

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    wordSet = set(wordDict)
    memo = {}

    def backtrack(start):
        if start in memo:
            return memo[start]

        sentences = []
        if start == len(s):
            sentences.append("")

        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in wordSet:
                for subsentence in backtrack(end):
                    sentences.append(word + (" " if subsentence else "") + subsentence)

        memo[start] = sentences
        return sentences

    return backtrack(0)

if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(wordBreak(s, wordDict))
