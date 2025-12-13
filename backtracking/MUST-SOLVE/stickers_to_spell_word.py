# Stickers to Spell Word
# Problem: https://leetcode.com/problems/stickers-to-spell-word/
# Solution:

from collections import Counter
from functools import lru_cache
from typing import List

def minStickers(stickers: List[str], target: str) -> int:
    sticker_counts = [Counter(sticker) for sticker in stickers]

    @lru_cache(None)
    def dfs(remaining):
        if not remaining:
            return 0

        target_count = Counter(remaining)
        result = float('inf')

        for sticker in sticker_counts:
            if sticker[remaining[0]] == 0:
                continue

            new_remaining = "".join(
                [char * max(0, target_count[char] - sticker[char]) for char in target_count]
            )

            result = min(result, 1 + dfs(new_remaining))

        return result

    result = dfs(target)
    return result if result != float('inf') else -1

if __name__ == "__main__":
    stickers = ["with", "example", "science"]
    target = "thehat"
    print(minStickers(stickers, target))
