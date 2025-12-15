# Valid Perfect Square
# Problem: https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
            
        left, right = 1, num // 2
        
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1
                
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPerfectSquare(16))  # Output: True
    print(solution.isPerfectSquare(14))  # Output: False
