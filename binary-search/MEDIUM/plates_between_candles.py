# Plates Between Candles
# Problem: https://leetcode.com/problems/plates-between-candles/

from typing import List
import bisect

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        candles = [i for i, c in enumerate(s) if c == '|']
        
        # Precompute prefix count of plates?
        # or calculate using candle positions.
        # Between candles[i] and candles[j], plates = (pos[j] - pos[i] - 1) - (j - i - 1)
        # = (pos[j] - pos[i]) - (j - i).
        
        ans = []
        for left, right in queries:
            # Find first candle >= left
            idx_l = bisect.bisect_left(candles, left)
            # Find last candle <= right
            idx_r = bisect.bisect_right(candles, right) - 1
            
            if idx_l < idx_r:
                pos_l = candles[idx_l]
                pos_r = candles[idx_r]
                # Count candles between them inclusive
                num_candles = idx_r - idx_l + 1
                length = pos_r - pos_l + 1
                plates = length - num_candles
                ans.append(plates)
            else:
                ans.append(0)
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.platesBetweenCandles("**|**|***|", [[2,5],[5,9]])) # [2, 3]
