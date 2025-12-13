# Letter Tile Possibilities
# Problem: https://leetcode.com/problems/letter-tile-possibilities/
# Solution:

from typing import List
from collections import Counter

def numTilePossibilities(tiles: str) -> int:
    def backtrack():
        nonlocal count
        for tile in tile_count:
            if tile_count[tile] > 0:
                count += 1
                tile_count[tile] -= 1
                backtrack()
                tile_count[tile] += 1

    tile_count = Counter(tiles)
    count = 0
    backtrack()
    return count

if __name__ == "__main__":
    tiles = "AAB"
    print(numTilePossibilities(tiles))
