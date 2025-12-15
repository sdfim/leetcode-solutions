# Find Maximum Non-decreasing Array Length
# Problem: https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

from typing import List
import collections

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        # We need to replace subarrays with their sums to form non-decreasing array.
        # Maximize length of resulting array.
        # DP[i] = max length of non-decreasing array ending at index i (using nums[0...i] converted).
        # To compute DP[i], we need to find transition j < i such that sum(nums[j+1...i]) >= last_element_of_chain_ending_at_j.
        # We want to Maximize length (DP[j] + 1).
        # Among those with max length, we want to Minimize the last element value to make it easier for future.
        # So state: dp[i] = (max_len, min_last_val).
        # Actually it's proven that maximizing length is equivalent to greedily minimizing last element value at each step locally?
        # Yes. If we can extend from j1 and j2, and len1 > len2, we prefer len1.
        # If len1 == len2, we prefer smaller last val.
        # AND it turns out `last_val` minimization correlates with length maximization.
        # If we just focus on: "Find j such that prefix_sum[i] - prefix_sum[j] >= last_val[j]".
        # maximize j? Closest j gives smallest sum[i]-sum[j] (which is risky) but we want to maximize *steps*.
        # Actually to maximize steps, we want sums to be small.
        # Smallest sums allow more elements.
        # So we want smallest valid sum.
        # Smallest valid sum corresponds to LARGEST valid j.
        # So we want largest j < i satisfying condition.
        
        # pre[i]: prefix sum.
        # Condition: pre[i] - pre[j] >= last_val[j]
        # pre[i] >= pre[j] + last_val[j]
        # Let target[j] = pre[j] + last_val[j].
        # We want largest j such that target[j] <= pre[i].
        # Since pre[i] is increasing (nums>0 usually? Yes), we can optimize.
        # Is target[j] monotonic? Not necessarily.
        # But we can maintain a monotonic queue or binary search on useful candidates.
        # Since we want LARGEST j, we only care about j's that might be valid.
        # If j1 < j2 and target[j1] >= target[j2], then j1 is useless?
        # Yes, because j2 is larger (better) and easier to satisfy (smaller target).
        # So we maintain indices j with increasing target[j].
        # Actually we want increasing j, increasing target?
        # Use Monotonic Stack/Queue?
        # We want largest j with target[j] <= val.
        # If we keep pairs (target, j) sorted by target or j?
        # If we keep j increasing, we eliminate j if target[j] >= target[j+1] (j+1 is better).
        # So we keep increasing j with INCREASING target.
        # Queue: j1, j2... targets increasing.
        # query pre[i]. We want largest j with target <= pre.
        # We can pop from left while target[q[1]] <= pre[i]?
        # Since pre[i] increases, we can permanently move start pointer.
        
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
            
        dp_len = [0] * (n + 1)
        last_val = [0] * (n + 1)
        
        # Deque stores indices j.
        # Invariant: target[j] is strictly increasing in deque.
        q = collections.deque([0])
        
        for i in range(1, n + 1):
            # Find largest j such that pre[j] + last_val[j] <= pre[i]
            # Since pre[i] grows, we can pop obsolete candidates from left?
            # We want largest j.
            # q[0] is smallest target. q[-1] is largest target.
            
            # Since q has increasing targets, and we want largest j satisfying condition:
            # We can binary search on q? Or linear scan if efficient?
            # Since pre[i] increases, valid range moves right.
            # But we want largest valid j.
            # If q[0] and q[1] both valid, q[1] is better.
            # So we remove q[0] if q[1] is valid.
            
            while len(q) > 1 and pre[q[1]] + last_val[q[1]] <= pre[i]:
                q.popleft()
                
            j = q[0]
            
            dp_len[i] = dp_len[j] + 1
            last_val[i] = pre[i] - pre[j]
            
            # Add i to deque
            # Maintain increasing target property.
            # target[i] = pre[i] + last_val[i].
            # Remove elements from right if target[q[-1]] >= target[i]
            # (Because i is larger index, so if target[i] <= target[old], i is strictly better).
            
            current_target = pre[i] + last_val[i]
            while q and (pre[q[-1]] + last_val[q[-1]] >= current_target):
                q.pop()
            q.append(i)
            
        return dp_len[n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaximumLength([5,2,2])) # Output: 1
