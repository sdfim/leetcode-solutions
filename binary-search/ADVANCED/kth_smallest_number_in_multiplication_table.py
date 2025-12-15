# Kth Smallest Number in Multiplication Table
# Problem: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_less_equal(x):
            count = 0
            for i in range(1, m + 1):
                # Count multiples of i less than equal to x
                # values in row i are i, 2i, 3i ... n*i
                # min(n, x // i) gives how many
                count += min(n, x // i)
            return count
            
        left, right = 1, m * n
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            if count_less_equal(mid) >= k:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthNumber(3, 3, 5))  # Output: 3
