# Minimum Garden Perimeter to Collect Enough Apples
# Problem: https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # On a square of size 2*n (coordinates -n to n),
        # Apples on the perimeter at distance d from origin (Manhattan) is... 
        # Total apples for side length 2n: S(n)
        # S(n) - S(n-1) is apples on the perimeter of square n.
        # Perimeter of square n (vertices (n,n), (n,-n), etc.)
        # Number of apples for a given n: 2 * n * (n+1) * (2n+1)
        # Wait, formula is 2*n*(n+1)*(2*n+1).
        # apples(n) = 2*n^3 + 3*n^2 + n? No.
        
        # Total apples in square size 2n:
        # Sum of |x| + |y| for -n <= x, y <= n? No.
        # The problem states apples at (x,y) is |x| + |y|.
        # Total apples inside square [-n, n] x [-n, n].
        # For a shell at radius n (square perimeter):
        # 12 * n^2.
        # Total(n) = Total(n-1) + 12 * n^2.
        # Total(n) = 12 * sum(k^2) = 12 * n(n+1)(2n+1)/6 = 2*n*(n+1)*(2n+1).
        
        # We need Total(n) >= neededApples.
        # Binary search for n.
        
        left, right = 1, 100000 # n=100000 => apples ~ 4*10^15, ample.
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            total = 2 * mid * (mid + 1) * (2 * mid + 1)
            if total >= neededApples:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans * 8 # Perimeter is 8*n

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumPerimeter(1)) # 8
    print(solution.minimumPerimeter(13)) # 16
