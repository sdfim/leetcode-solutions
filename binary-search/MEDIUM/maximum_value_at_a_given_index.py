# Maximum Value at a Given Index in a Bounded Array
# Problem: https://leetcode.com/problems/maximum-value-at-a-given-index/

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def get_sum(val):
            # Sum of pyramid with peak val at index
            # Left side: val-1, val-2, ..., down to 1 or 0
            # Length to left is index + 1 including val itself? 
            # Actually simpler: count elements on left = index, right = n - 1 - index
            
            # Peak is val.
            # Left counts: index elements. Values: val-1, val-2...
            # If val > index: sum is arithmetic.
            # If val <= index: arithmetic down to 1, then rest 1s.
            
            # Left sum (excluding peak):
            left_count = index
            if val > left_count:
                # arithmetic sum from val-1 down to val-left_count
                # len = left_count, end = val - left_count
                # sum = (start + end) * len / 2
                s_left = (val - 1 + val - left_count) * left_count // 2
            else:
                # val-1 down to 1, plus ones
                s_left = (val - 1) * val // 2 + (left_count - (val - 1))
            
            # Right sum (excluding peak):
            right_count = n - 1 - index
            if val > right_count:
                s_right = (val - 1 + val - right_count) * right_count // 2
            else:
                s_right = (val - 1) * val // 2 + (right_count - (val - 1))
                
            return s_left + s_right + val
            
        # Binary search for val
        # Min val is 1 (positive integers). Max val is maxSum.
        left, right = 1, maxSum
        res = 1
        
        while left <= right:
            mid = (left + right) // 2
            if get_sum(mid) <= maxSum:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxValue(4, 2, 6))  # Output: 2
