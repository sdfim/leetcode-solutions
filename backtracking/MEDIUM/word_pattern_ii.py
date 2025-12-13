# Word Pattern II
# Problem: https://leetcode.com/problems/word-pattern-ii/
# Solution:

from typing import Dict

def wordPatternMatch(pattern: str, s: str) -> bool:
    def backtrack(p_index, s_index):
        if p_index == len(pattern) and s_index == len(s):
            return True
        if p_index == len(pattern) or s_index == len(s):
            return False

        char = pattern[p_index]
        if char in mapping:
            word = mapping[char]
            if not s.startswith(word, s_index):
                return False
            return backtrack(p_index + 1, s_index + len(word))

        for end in range(s_index + 1, len(s) + 1):
            word = s[s_index:end]
            if word in used:
                continue

            mapping[char] = word
            used.add(word)
            if backtrack(p_index + 1, end):
                return True
            del mapping[char]
            used.remove(word)

        return False

    mapping: Dict[str, str] = {}
    used = set()
    return backtrack(0, 0)

if __name__ == "__main__":
    pattern = "abab"
    s = "redblueredblue"
    print(wordPatternMatch(pattern, s))
