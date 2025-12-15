# 132 Pattern
# Problem: https://leetcode.com/problems/132-pattern/

from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # We need i < j < k and nums[i] < nums[k] < nums[j]
        # We can iterate 'j' from right to left?
        # Standard solution is stack based O(N).
        # Binary search approach:
        # Iterate j, keep track of min_i (nums[i] < nums[j]).
        # Then we need to find if there is a k > j such that min_i < nums[k] < nums[j]
        # We can maintain a sorted list of k values? (SortedList or similar)
        
        if len(nums) < 3:
            return False
            
        min_prefix = [nums[0]]
        for i in range(1, len(nums)):
            min_prefix.append(min(min_prefix[-1], nums[i]))
            
        stack = [] # Acts as potential k values
        
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > min_prefix[j]:
                # We have a valid 'i' and 'j' condition: nums[i] < nums[j]
                # Now check stack for 'k'
                while stack and stack[-1] <= min_prefix[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
                
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.find132pattern([1,2,3,4]))  # Output: False
    print(solution.find132pattern([3,1,4,2]))  # Output: True
