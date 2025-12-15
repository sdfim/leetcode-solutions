# Find the Duplicate Number
# Problem: https://leetcode.com/problems/find-the-duplicate-number/

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Binary Search on Value approach (O(N log N)) to meet O(1) space constraints usually required
        # Or Floyd's Cycle Detection (O(N)) which fits "Linked List" patterns but also works here.
        # Since this is "Binary Search" folder, I'll use the BS on Value method.
        
        low, high = 1, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Count how many numbers are <= mid
            count = 0 
            for num in nums:
                if num <= mid:
                    count += 1
            
            if count > mid:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.findDuplicate([1,3,4,2,2]))  # Output: 2
