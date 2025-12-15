# Minimize the Maximum of Two Arrays
# Problem: https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

import math

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        # Binary search for the maximum value X.
        # We need to pick uniqueCnt1 numbers for Set1 and uniqueCnt2 for Set2 from range [1, X].
        # Set1 cannot contain multiples of divisor1.
        # Set2 cannot contain multiples of divisor2.
        
        # Count available numbers in [1, X]:
        # A = numbers NOT divisible by divisor1. (Can go to Set1)
        # B = numbers NOT divisible by divisor2. (Can go to Set2)
        # C = numbers NOT divisible by LCM(divisor1, divisor2). (Can go to Set1 OR Set2)
        
        # Wait.
        # Total items in [1, X] available for Set1: X - X // divisor1.
        # Total items in [1, X] available for Set2: X - X // divisor2.
        # Items available for BOTH? No.
        # Items excluded from Set1 (div by d1) but usable in Set2? (div by d1 but NOT d2).
        # Items excluded from Set2 (div by d2) but usable in Set1? (div by d2 but NOT d1).
        # Items usable in BOTH (div by neither d1 nor d2). Count = X - X // d1 - X // d2 + X // lcm.
        # Actually simple logic:
        # We must satisfy:
        # 1. Available for Set1 >= uniqueCnt1.
        # 2. Available for Set2 >= uniqueCnt2.
        # 3. Total Available (in union) >= uniqueCnt1 + uniqueCnt2.
        # Total available = X - (numbers divisible by BOTH d1 and d2).
        # i.e., X - X // lcm.
        
        lcm_val = math.lcm(divisor1, divisor2)
        
        def check(x):
            cnt1 = x - x // divisor1
            cnt2 = x - x // divisor2
            total = x - x // lcm_val
            return cnt1 >= uniqueCnt1 and cnt2 >= uniqueCnt2 and total >= uniqueCnt1 + uniqueCnt2
            
        left, right = 1, 10**10
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
    print(solution.minimizeSet(2, 7, 1, 3)) # 4
