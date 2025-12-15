# Sum of Floored Pairs
# Problem: https://leetcode.com/problems/sum-of-floored-pairs/

from typing import List

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        if not nums: return 0
        
        max_val = max(nums)
        # Frequency array
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
            
        # Prefix sum of frequencies
        prefix = [0] * (max_val + 2)
        for i in range(1, max_val + 2):
            prefix[i] = prefix[i-1] + freq[i-1]
            
        res = 0
        
        # Iterate over distinct numbers present in nums
        for i in range(1, max_val + 1):
            if freq[i] > 0:
                # Iterate multiples of i
                # For numbers in [j, j + i - 1], floor(val / i) is constant = j / i
                for j in range(i, max_val + 1, i):
                    upper = min(j + i - 1, max_val)
                    # Count elements in range [j, upper]
                    count = prefix[upper + 1] - prefix[j]
                    
                    if count > 0:
                        term = (j // i) * count
                        res = (res + term * freq[i]) % MOD
        
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfFlooredPairs([2,5,9])) # Output: 10
