# Maximize Score of Numbers in Ranges
# Problem: https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

from typing import List

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        n = len(start)
        
        def check(score):
            # Try to pick x0, x1... such that xi - x(i-1) >= score
            # and xi in [start[i], start[i] + d]
            
            last_val = start[0] # Pick as small as possible for first?
            # Actually, we can pick any x0 in range. To maximize future chances, pick smallest x0?
            # Yes, picking strictly larger x0 only constrains next moves.
            
            for i in range(1, n):
                # We need x_i >= last_val + score
                target = last_val + score
                
                # Available range: [start[i], start[i] + d]
                if target > start[i] + d:
                    return False
                    
                # We pick smallest valid x_i
                picked = max(target, start[i])
                last_val = picked
                
            return True
            
        left, right = 0, 2 * 10**9 + d # Max possible gap
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxPossibleScore([6,0,3], 2)) # 4
