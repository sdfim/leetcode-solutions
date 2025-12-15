# Maximize Win From Two Segments
# Problem: https://leetcode.com/problems/maximize-win-from-two-segments/

from typing import List

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        # dp[i] = max prizes we can collect with ONE segment ending at or before index i (in prizePositions)
        # We need to choose 2 segments.
        # Segment 2 ends at 'right'. Segment 1 ends before Segment 2 starts.
        
        n = len(prizePositions)
        dp = [0] * (n + 1)
        ans = 0
        left = 0
        
        for right in range(n):
            # Maintain window [left, right] such that positions[right] - positions[left] <= k
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
                
            current_window_count = right - left + 1
            
            # Best we can do with previous segment is dp[left-1] (using 1-based dp for convenience) or dp[left]
            # dp[i] stores max for one segment using first i elements (0 to i-1)
            
            # dp[left] corresponds to max prizes using elements 0...left-1
            # Current segment uses left...right.
            ans = max(ans, current_window_count + dp[left])
            
            # Update dp[right+1]
            dp[right+1] = max(dp[right], current_window_count)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximizeWin([1,1,2,2,3,3,5], 2)) # 7
