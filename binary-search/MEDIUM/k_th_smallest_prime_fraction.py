# K-th Smallest Prime Fraction
# Problem: https://leetcode.com/problems/k-th-smallest-prime-fraction/

from typing import List
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Heap approach (Priority Queue)
        # Or Binary Search on Value (0.0 to 1.0)
        
        n = len(arr)
        left, right = 0.0, 1.0
        
        while left < right:
            mid = (left + right) / 2
            
            # Count fractions <= mid
            max_f = [0, 1]
            total = 0
            j = 1
            
            for i in range(n - 1):
                while j < n and arr[i] > mid * arr[j]:
                    j += 1
                total += (n - j)
                if j < n:
                    if arr[i] * max_f[1] > arr[j] * max_f[0]:
                        max_f = [arr[i], arr[j]]
            
            if total == k:
                return max_f
            elif total < k:
                left = mid
            else:
                # We need fewer elements, so smaller fraction
                # Wait, if total > k, we have too many, so we need smaller threshold?
                # Yes, if we have too many fractions <= mid, we need to lower mid.
                right = mid 
        
        return []

if __name__ == "__main__":
    solution = Solution()
    print(solution.kthSmallestPrimeFraction([1,2,3,5], 3))  # Output: [2, 5]
