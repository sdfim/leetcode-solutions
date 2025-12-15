# Minimum Time to Activate String
# Problem: https://leetcode.com/problems/minimum-time-to-activate-string/

from typing import List

class Solution:
    def minTimeToActivate(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total_substrings = n * (n + 1) // 2
        
        def check(t):
            # Stars at indices order[0...t] (inclusive? t is time steps? starting t=0 means 1 char?
            # Problem says "Minimum Time t". If t=0, 1st char replaced.
            # So indices order[0 ... t].
            
            indices = sorted(order[:t+1])
            
            # Calculate invalid (gap based)
            # Gaps of non-star characters.
            # Indices represent Stars.
            # Between -1 and indices[0], gap len = indices[0] - (-1) - 1.
            
            invalid = 0
            prev = -1
            for idx in indices:
                gap = idx - prev - 1
                if gap > 0:
                    invalid += gap * (gap + 1) // 2
                prev = idx
            
            gap = n - prev - 1
            if gap > 0:
                invalid += gap * (gap + 1) // 2
                
            return total_substrings - invalid >= k
            
        left, right = 0, n - 1
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minTimeToActivate("abc", [1,0,2], 2)) # 0
