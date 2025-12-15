# Count Elements With At Least K Greater Values
# Problem: https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

from typing import List
import bisect

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(nums)
            
        nums.sort()
        n = len(nums)
        
        if k >= n:
            return 0
            
        # Elements at indices n-k, n-k+1, ..., n-1 are the k largest.
        # Let T = nums[n-k].
        # Any element strictly less than T will have at least k greater elements (the ones >= T).
        # Actually, if duplicate values exist, say [1, 2, 2, 3], k=1.
        # n=4. n-k = 3. nums[3]=3. T=3.
        # Elements < 3: 1, 2, 2.
        # 2 < 3, count 1 greater. Yes.
        # 1 < 3, count 1 greater (actually 3 greater). Yes.
        # What if nums=[5,5,5], k=1.
        # n=3. n-k=2. nums[2]=5. T=5.
        # Elements < 5: 0.
        # Correct, no element has a strictly greater element.
        
        # What if nums=[1, 2, 3], k=2.
        # n=3. n-k=1. nums[1]=2. T=2.
        # Elements < 2: 1.
        # 1 has 2 and 3 greater. Correct.
        
        thresh = nums[n-k]
        
        # Using bisect_left to find count of elements < thresh
        return bisect.bisect_left(nums, thresh)

if __name__ == "__main__":
    solution = Solution()
    print(solution.countElements([3,1,2], 1)) # 2
    print(solution.countElements([5,5,5], 2)) # 0
