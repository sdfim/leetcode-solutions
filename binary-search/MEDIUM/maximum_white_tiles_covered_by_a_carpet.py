# Maximum White Tiles Covered by a Carpet
# Problem: https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

from typing import List
import bisect

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        
        # Prefix sum of tile lengths
        prefix = [0] * (n + 1)
        start_pos = []
        for i in range(n):
            prefix[i+1] = prefix[i] + (tiles[i][1] - tiles[i][0] + 1)
            start_pos.append(tiles[i][0])
            
        ans = 0
        for i in range(n):
            # Try placing carpet starting at tiles[i][0]
            start = tiles[i][0]
            end = start + carpetLen - 1
            
            # Find index of first tile ending <= end?
            # Actually find first tile starting > end, then go back.
            # We want tiles fully or partially covered.
            
            # Find rightmost tile that starts within range [start, end].
            idx = bisect.bisect_right(start_pos, end) - 1
            
            # Tiles from i to idx are at least partially covered.
            # Full cover from i to idx?
            # Range covered:
            # Full tiles count: prefix[idx+1] - prefix[i].
            # But the last tile `idx` might extend beyond `end`.
            # We need to subtract the part outside.
            
            cover = prefix[idx+1] - prefix[i]
            
            # Adjustment for last tile
            if tiles[idx][1] > end:
                extra = tiles[idx][1] - end
                cover -= extra
                
            ans = max(ans, cover)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumWhiteTiles([[1,5],[10,11],[12,18],[20,25],[30,32]], 10)) # 9
