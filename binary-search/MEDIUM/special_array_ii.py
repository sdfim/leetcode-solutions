# Special Array II
# Problem: https://leetcode.com/problems/special-array-ii/

from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # A pair (i, i+1) is bad if nums[i]%2 == nums[i+1]%2.
        # Precompute bad indices.
        n = len(nums)
        bad = [0] * n
        for i in range(n - 1):
            if nums[i] % 2 == nums[i+1] % 2:
                bad[i] = 1 # index i is the start of a bad pair
                
        # Prefix sum of bad
        prefix_bad = [0] * (n + 1)
        for i in range(n):
            prefix_bad[i+1] = prefix_bad[i] + bad[i]
            
        ans = []
        for u, v in queries:
            # Check range [u, v-1]. If any bad, then False.
            if u == v:
                ans.append(True)
                continue
                
            count = prefix_bad[v] - prefix_bad[u]
            ans.append(count == 0)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.isArraySpecial([3,4,1,2,6], [[0,4]])) # False (2,6 both even)
    print(solution.isArraySpecial([4,3,1,6], [[0,2], [2,3]])) # [False, True]?
    # 4(e) 3(o) 1(o) -> 3,1 bad. 0-2 -> range check indices 0,1. bad at 1. count=1. False.
    # 2-3 -> 1(o) 6(e). Ok. True.
