# Verbal Arithmetic Puzzle
# Problem: https://leetcode.com/problems/verbal-arithmetic-puzzle/
# Solution:

from typing import List

def isSolvable(words: List[str], result: str) -> bool:
    def backtrack(index, carry):
        if index == max_len:
            return carry == 0

        total = carry
        for word in words:
            if len(word) > index:
                total += mapping[word[-1 - index]]

        if len(result) > index:
            total -= mapping[result[-1 - index]]

        if total % 10 != 0:
            return False

        return backtrack(index + 1, total // 10)

    unique_chars = set("".join(words) + result)
    if len(unique_chars) > 10:
        return False

    mapping = {}
    max_len = max(len(word) for word in words + [result])
    return backtrack(0, 0)

if __name__ == "__main__":
    words = ["SEND", "MORE"]
    result = "MONEY"
    print(isSolvable(words, result))
