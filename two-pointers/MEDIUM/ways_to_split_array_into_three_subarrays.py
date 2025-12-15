# Ways to Split Array Into Three Subarrays
# Problem: https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
# Solution:

from typing import List
import bisect

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
            
        ans = 0
        mod = 10**9 + 7
        
        for i in range(1, n - 1): # i is first split point (exclusive for first part)
            if prefix[i] * 3 > prefix[n]:
                break
                
            # Find range for second split j
            # Condition 1: prefix[j] - prefix[i] >= prefix[i] -> prefix[j] >= 2 * prefix[i]
            # Condition 2: prefix[n] - prefix[j] >= prefix[j] - prefix[i] -> prefix[j] <= (prefix[n] + prefix[i]) // 2
            
            l = bisect.bisect_left(prefix, 2 * prefix[i], i + 1, n)
            r = bisect.bisect_right(prefix, (prefix[n] + prefix[i]) // 2, i + 1, n)
            
            if r > l:
                ans = (ans + r - l) % mod
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,1,1]
    print(f"Ways to split {nums1}: {solution.waysToSplit(nums1)}")
    
    nums2 = [1,2,2,2,5,0]
    print(f"Ways to split {nums2}: {solution.waysToSplit(nums2)}")
