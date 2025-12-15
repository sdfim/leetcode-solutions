# Shortest Subarray with Sum at Least K
# Problem: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

from typing import List
import collections

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
            
        # Monotonic Deque
        # Stores indices i such that prefix[i] is increasing
        # We want smallest j - i such that prefix[j] - prefix[i] >= k
        
        q = collections.deque()
        res = n + 1
        
        for y, py in enumerate(prefix):
            # Check if we can satisfy condition with current y and some previous x in deque
            while q and py - prefix[q[0]] >= k:
                res = min(res, y - q.popleft())
                
            # Maintain increasing order of prefix sums
            while q and py <= prefix[q[-1]]:
                q.pop()
                
            q.append(y)
            
        return res if res <= n else -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestSubarray([2,-1,2], 3))  # Output: 3
