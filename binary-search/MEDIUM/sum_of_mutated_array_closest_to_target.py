# Sum of Mutated Array Closest to Target
# Problem: https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

from typing import List
import bisect

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
            
        def calculate_sum(value):
            idx = bisect.bisect_left(arr, value)
            # Elements < value are kept as is: sum is prefix[idx]
            # Elements >= value are changed to value: count is (n - idx), sum is (n-idx)*value
            return prefix[idx] + (n - idx) * value
            
        left, right = 0, max(arr)
        res = 0
        min_diff = float('inf')
        
        # We can also do binary search to find optimal value
        # But simply iterating or ternary search works since the function is convex-like?
        # Actually it's monotonic increasing sum wrt value.
        # So we can just binary search for the value that gives sum closest to target.
        
        while left <= right:
            mid = (left + right) // 2
            s = calculate_sum(mid)
            if s < target:
                left = mid + 1
            else:
                right = mid - 1
            
            diff = abs(s - target)
            if diff < min_diff or (diff == min_diff and mid < res):
                min_diff = diff
                res = mid
                
        # The binary search above finds one candidate, but might miss local optimum if we just update res greedily?
        # A better way for monotonic function close to target:
        # Find the first value where sum >= target usually gives upper bound.
        # Check that value and value-1.
        
        # Proper BS:
        l, r = 0, max(arr)
        while l < r:
            mid = (l + r) // 2
            if calculate_sum(mid) < target:
                l = mid + 1
            else:
                r = mid
        
        val1 = l
        val2 = l - 1
        
        sum1 = calculate_sum(val1)
        sum2 = calculate_sum(val2)
        
        if abs(sum2 - target) <= abs(sum1 - target):
            return val2
        return val1

if __name__ == "__main__":
    solution = Solution()
    print(solution.findBestValue([4,9,3], 10))  # Output: 3
