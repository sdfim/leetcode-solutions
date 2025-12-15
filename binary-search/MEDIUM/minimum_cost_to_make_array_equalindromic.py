# Minimum Cost to Make Array Equalindromic
# Problem: https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # Median minimizes L1 distance
        median = nums[n // 2]
        
        # Find palindromes closest to median
        def get_pals(val):
            s = str(val)
            l = len(s)
            candidates = set()
            
            # Form palindromes by modifying prefix
            # Example: 123 -> 121, 131?
            # Standard approach: take prefix of length ceil(L/2), +0, +1, -1. Mirror it.
            prefix = int(s[:(l + 1) // 2])
            for d in [-1, 0, 1]:
                p = str(prefix + d)
                if l % 2 == 0:
                    cand = int(p + p[::-1])
                else:
                    cand = int(p + p[:-1][::-1])
                candidates.add(cand)
                
            # Edge cases: 99...9 or 100...001 for length change
            candidates.add(10**(l-1) - 1)
            candidates.add(10**l + 1)
            
            return candidates
            
        pals = get_pals(median)
        # Also check median of even length? nums[n//2 - 1]
        
        min_cost = float('inf')
        for p in pals:
            cost = sum(abs(x - p) for x in nums)
            min_cost = min(min_cost, cost)
            
        return min_cost

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumCost([1,2,3,4,5]))  # Output: 6 (pal=3)
