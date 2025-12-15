# Find the Number of Subarrays Where Boundary Elements Are Maximum
# Problem: https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        # We want pairs (i, j) s.t. nums[i] == nums[j] and max(nums[i..j]) == nums[i].
        # Monotonic stack.
        # Store elements (val, count) in decreasing order.
        # When processing x:
        # Pop elements < x. They can't form valid pair with element >= x (since x blocks them).
        # Check if top is == x. If so, add their count to answer, increment count.
        # Push x.
        
        stack = [] # (val, count)
        ans = 0
        
        for x in nums:
            while stack and stack[-1][0] < x:
                stack.pop()
                
            if stack and stack[-1][0] == x:
                prev_count = stack[-1][1]
                ans += prev_count
                stack[-1] = (x, prev_count + 1)
            else:
                stack.append((x, 1))
                
            # Every element forms a valid subarray with itself
            ans += 1
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfSubarrays([1,4,3,3,2])) # Output: 6
