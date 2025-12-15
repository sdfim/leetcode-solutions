# Preimage Size of Factorial Zeroes Function
# Problem: https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # f(x) = number of trailing zeros in x!
        # f(x) is non-decreasing.
        # We want count of x s.t. f(x) == k.
        # Since f(x) jumps (sometimes by >1 if multiple factors of 5 appear at once, e.g. at 25),
        # solution is either 5 or 0.
        
        # Binary search for x such that f(x) >= k.
        
        def count_zeros(n):
            count = 0
            while n > 0:
                n //= 5
                count += n
            return count
            
        def find_min_x(target):
            # Binary search range?
            # Max K is 10^9. 5 * 10^9 roughly.
            left, right = 0, 5 * (target + 1)
            res = -1
            while left <= right:
                mid = (left + right) // 2
                z = count_zeros(mid)
                if z >= target:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return res
            
        start = find_min_x(k)
        if count_zeros(start) != k:
            return 0
        
        # Next breakpoint
        end = find_min_x(k + 1)
        return end - start

if __name__ == "__main__":
    solution = Solution()
    print(solution.preimageSizeFZF(0))  # Output: 5
