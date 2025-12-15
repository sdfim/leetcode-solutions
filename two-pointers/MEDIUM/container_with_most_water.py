# Container With Most Water
# Problem: https://leetcode.com/problems/container-with-most-water/
# Solution:

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find two lines that together with the x-axis form a container,
        such that the container contains the most water.
        """
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            h = min(height[left], height[right])
            max_water = max(max_water, width * h)
            
            # Move the pointer with the smaller height,
            # because moving the taller one can only decrease area (width decreases, height at best stays same)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    height1 = [1,8,6,2,5,4,8,3,7]
    print(f"Max area for {height1}: {solution.maxArea(height1)}")
    
    height2 = [1,1]
    print(f"Max area for {height2}: {solution.maxArea(height2)}")
