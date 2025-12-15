# Ways to Split Array Into Three Subarrays
# Problem: https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

from typing import List
import bisect

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
            
        # Iterate first split point i (1-based end of first part)
        # 1st part: prefix[i]
        # We need to find range of j (end of 2nd part)
        # Conditions:
        # left <= mid: prefix[i] <= prefix[j] - prefix[i]  => prefix[j] >= 2 * prefix[i]
        # mid <= right: prefix[j] - prefix[i] <= prefix[n] - prefix[j] => 2*prefix[j] <= prefix[n] + prefix[i]
        
        mod = 10**9 + 7
        count = 0
        
        for i in range(1, n - 1): # i can go up to n-2 (leaving 2 elements)
            # Find leftmost j such that prefix[j] >= 2 * prefix[i]
            # Valid j starts at i + 1
            
            # Using bisect on prefix array
            # lower bound for j
            l_val = 2 * prefix[i]
            j_start = bisect.bisect_left(prefix, l_val)
            j_start = max(j_start, i + 1)
            
            # upper bound for j
            # 2*prefix[j] <= total + prefix[i]
            # prefix[j] <= (total + prefix[i]) / 2
            
            r_val = (prefix[n] + prefix[i]) // 2
            j_end = bisect.bisect_right(prefix, r_val) - 1
            j_end = min(j_end, n - 1)
            
            if j_start <= j_end:
                count = (count + (j_end - j_start + 1)) % mod
                
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.waysToSplit([1,1,1]))  # Output: 1
    print(solution.waysToSplit([1,2,2,2,5,0]))  # Output: 3
