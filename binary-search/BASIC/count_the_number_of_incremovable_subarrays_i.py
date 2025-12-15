# Count the Number of Incremovable Subarrays I
# Problem: https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            for j in range(i, n):
                # Remove subarray nums[i...j]
                # Check if remaining parts are strictly increasing
                
                temp = nums[:i] + nums[j+1:]
                
                is_increasing = True
                for k in range(len(temp) - 1):
                    if temp[k] >= temp[k+1]:
                        is_increasing = False
                        break
                
                if is_increasing:
                    ans += 1
                    
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.incremovableSubarrayCount([1,2,3,4]))  # Output: 10
    print(solution.incremovableSubarrayCount([6,5,7,8]))  # Output: 7
