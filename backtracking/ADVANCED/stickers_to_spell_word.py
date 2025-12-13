# Stickers to Spell Word
# Problem: https://leetcode.com/problems/stickers-to-spell-word/
# Solution:

from typing import List
from collections import Counter

def minStickers(stickers: List[str], target: str) -> int:
    def dfs(remaining):
        if not remaining:
            return 0
        if remaining in memo:
            return memo[remaining]

        target_count = Counter(remaining)
        min_stickers = float("inf")
        for sticker in sticker_counts:
            if sticker[remaining[0]] == 0:
                continue

            new_remaining = "".join(
                [char * max(0, target_count[char] - sticker[char]) for char in target_count]
            )
            min_stickers = min(min_stickers, 1 + dfs(new_remaining))

        memo[remaining] = min_stickers
        return memo[remaining]

    sticker_counts = [Counter(sticker) for sticker in stickers]
    memo = {}
    result = dfs(target)
    return result if result != float("inf") else -1

if __name__ == "__main__":
    stickers = ["with", "example", "science"]
    target = "thehat"
    print(minStickers(stickers, target))
