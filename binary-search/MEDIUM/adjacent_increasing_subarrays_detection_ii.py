# Adjacent Increasing Subarrays Detection II
# Problem: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        
        # f[i] = length of strictly increasing subarray STARTING at i
        f = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                f[i] = f[i+1] + 1
            else:
                f[i] = 1
                
        # We need max k such that there exists i where f[i] >= k and f[i+k] >= k.
        # This implies array at i...i+k-1 is increasing (length k)
        # And array at i+k...i+2k-1 is increasing (length k)
        # And they are adjacent.
        
        # Binary search for k. Range [1, n//2].
        left, right = 1, n // 2
        ans = 0 # If n < 2, ans 0? Subarray length usually >= 1. 
        # Actually single element is increasing subarray len 1.
        # If n=1, can't have 2 adjacent. ans=0.
        # If n=2, [1, 2] -> increasing len 2. But we need TWO adjacent.
        # [2, 1] -> [2], [1]. Len 1 adjacent.
        
        if n < 2: return 0
        ans = 0 # Default? Maybe 0 if impossible. But length 1 is always possible for n>=2.
        
        # Actually, iterate k is inefficient if we do full scan.
        # But we can check(k) in O(N).
        # Total O(N log N).
        
        while left <= right:
            mid = (left + right) // 2
            
            # check(mid)
            possible = False
            for i in range(n - 2 * mid + 1):
                if f[i] >= mid and f[i+mid] >= mid:
                    possible = True
                    break
            
            if possible:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1])) # 3
