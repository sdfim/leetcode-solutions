# Separate Black and White Balls
# Problem: https://leetcode.com/problems/separate-black-and-white-balls/
# Solution:

class Solution:
    def minimumSteps(self, s: str) -> int:
        swap_count = 0
        black_count = 0
        
        for char in s:
            if char == '1': # Black ball
                black_count += 1
            else: # White ball
                swap_count += black_count
                
        return swap_count

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "101"
    print(f"Steps for '{s1}': {solution.minimumSteps(s1)}")
    
    s2 = "100"
    print(f"Steps for '{s2}': {solution.minimumSteps(s2)}")
