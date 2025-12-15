# Trapping Rain Water
# Problem: https://leetcode.com/problems/trapping-rain-water/
# Solution:

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1,
        compute how much water it can trap after raining.
        """
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                
        return water

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"Trapped water for {height1}: {solution.trap(height1)}")
    
    height2 = [4,2,0,3,2,5]
    print(f"Trapped water for {height2}: {solution.trap(height2)}")
