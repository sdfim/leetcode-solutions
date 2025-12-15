# Numbers At Most N Given Digit Set
# Problem: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

from typing import List
import bisect

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        k = len(s)
        digits_len = len(digits)
        
        count = 0
        # 1. Count numbers with fewer digits than n
        for i in range(1, k):
            count += digits_len ** i
            
        # 2. Count numbers with same length k
        for i in range(k):
            # Check how many digits in our set are strictly smaller than s[i]
            # Since digits is sorted string list
            # We can use bisect? Need to convert s[i] to same type? digits are strings.
            digit_char = s[i]
            
            # Find number of candidates smaller than digit_char
            # We can just iterate or bisect
            idx = bisect.bisect_left(digits, digit_char)
            # All digits[:idx] are strictly smaller
            # For each such choice, we have (k - 1 - i) remaining positions
            count += idx * (digits_len ** (k - 1 - i))
            
            # If current digit s[i] is NOT in our set, we can't continue matching prefix
            if idx == len(digits) or digits[idx] != digit_char:
                return count
                
            # If it matches, we continue to next position
            # If we reached the end (matched all prefix), then the number n itself is valid
            if i == k - 1:
                count += 1
                
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.atMostNGivenDigitSet(["1","3","5","7"], 100)) # Output: 20
