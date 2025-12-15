# Arranging Coins
# Problem: https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # k * (k + 1) / 2 <= n
        # Solve for k
        left, right = 1, n
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            curr = mid * (mid + 1) // 2
            if curr == n:
                return mid
            elif curr < n:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.arrangeCoins(5))  # Output: 2
    print(solution.arrangeCoins(8))  # Output: 3
