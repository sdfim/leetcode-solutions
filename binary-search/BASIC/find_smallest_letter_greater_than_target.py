# Find Smallest Letter Greater Than Target
# Problem: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # If target is greater than or equal to the last character, wrap around
        if target >= letters[-1]:
            return letters[0]
            
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                
        return letters[left]

if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreatestLetter(["c","f","j"], "a"))  # Output: "c"
    print(solution.nextGreatestLetter(["c","f","j"], "c"))  # Output: "f"
