# Sqrt(x)
# Problem: https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 1, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1
                
        return right

if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(4))  # Output: 2
    print(solution.mySqrt(8))  # Output: 2
