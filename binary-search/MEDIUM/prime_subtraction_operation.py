# Prime Subtraction Operation
# Problem: https://leetcode.com/problems/prime-subtraction-operation/

from typing import List
import bisect

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Sieve primes up to 1000
        primes = []
        is_prime = [True] * 1001
        for i in range(2, 1001):
            if is_prime[i]:
                primes.append(i)
                for j in range(i*i, 1001, i):
                    is_prime[j] = False
                    
        # Greedy
        # We want to make nums strictly increasing.
        # nums[i] should be as small as possible but larger than nums[i-1].
        # So we pick largest prime p such that nums[i] - p > prev.
        # nums[i] - p > prev  =>  p < nums[i] - prev.
        
        prev = 0
        for n in nums:
            limit = n - prev
            # We want largest prime < limit
            idx = bisect.bisect_left(primes, limit)
            # primes[idx] >= limit. We need primes[idx-1].
            
            if idx > 0:
                p = primes[idx - 1]
                n -= p
            
            if n <= prev:
                return False
            prev = n
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.primeSubOperation([4,9,6,10]))  # Output: True (4-3=1, 9-7=2, 6-3=3, 10 -> 1,2,3,10)
