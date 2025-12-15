# Minimum Operations to Make Binary Palindrome
# Problem: https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        # Precompute binary palindromes
        # nums[i] <= 5000.
        # Max value roughly 5000 approx 2^13. 
        # So we check palindromes up to 2^14 or slightly more.
        
        palindromes = []
        
        # Generate binary palindromes
        # Length 1 to 15 (covers up to 32768)
        
        for length in range(1, 16):
            # Construct first half
            half_len = (length + 1) // 2
            # Iterate all numbers of bit-length half_len
            start = 1 << (half_len - 1)
            end = (1 << half_len) - 1
            
            for half in range(start, end + 1):
                # Construct full palindrome
                s = bin(half)[2:]
                if length % 2 == 1:
                    full_s = s + s[:-1][::-1]
                else:
                    full_s = s + s[::-1]
                
                val = int(full_s, 2)
                palindromes.append(val)
                
        palindromes.sort()
        
        # Add 0? "excluding leading zeros". 0 is "0" -> palindrome.
        if 0 not in palindromes:
            palindromes.insert(0, 0)
            
        import bisect
        ans = []
        for x in nums:
            idx = bisect.bisect_left(palindromes, x)
            dist = float('inf')
            
            if idx < len(palindromes):
                dist = min(dist, abs(palindromes[idx] - x))
            if idx > 0:
                dist = min(dist, abs(palindromes[idx-1] - x))
                
            ans.append(dist)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([1, 2, 4])) # [0, 1, 1]
    print(solution.minOperations([6, 7, 12])) # [1, 0, 3] -> 12(1100)->15(1111) dist 3.
