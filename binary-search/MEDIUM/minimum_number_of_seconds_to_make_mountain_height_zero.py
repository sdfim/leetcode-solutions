# Minimum Number of Seconds to Make Mountain Height Zero
# Problem: https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

from typing import List
import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Determine minimum time T such that total height reduction >= mountainHeight.
        # For a worker with base time w, if they work for x units of height, time taken is:
        # w * (1 + 2 + ... + x) = w * x(x+1)/2.
        # Given time T, max x?
        # w * x(x+1)/2 <= T
        # x^2 + x - 2T/w <= 0.
        # Roots: (-1 + sqrt(1 + 8T/w)) / 2.
        # x = floor((-1 + sqrt(1 + 8T/w)) / 2).
        
        def check(T):
            total_h = 0
            for w in workerTimes:
                # w * x(x+1)/2 <= T
                # 1 + 8T/w might overflow if not careful, but T is up to maybe 10^16? 
                # workerTimes ~ 1000, mountainHeight ~ 10^5. 
                # If only 1 worker with w=1000, height 10^5.
                # 1000 * 10^5 * 10^5 / 2 approx 5 * 10^12. Fits in 64-bit float/int.
                
                val = 1 + 8 * T / w
                x = int((math.isqrt(int(val * 100)) / 10 - 1) / 2) 
                # Better integer math:
                # x(x+1) <= 2T/w.
                # discriminanat D = 1 + 8*(T//w).
                # x = (math.isqrt(D) - 1) // 2.
                
                D = 1 + 8 * (T // w)
                x = (math.isqrt(D) - 1) // 2
                total_h += x
                if total_h >= mountainHeight:
                    return True
            return total_h >= mountainHeight
            
        left, right = 1, 10**18
        ans = right
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
    print(solution.minNumberOfSeconds(4, [2,1,1])) # 3
