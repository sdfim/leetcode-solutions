# Minimum Number of Swaps to Make the String Balanced
# Problem: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
# Solution:

class Solution:
    def minSwaps(self, s: str) -> int:
        stack_size = 0
        for c in s:
            if c == '[':
                stack_size += 1
            else:
                if stack_size > 0:
                    stack_size -= 1
        return (stack_size + 1) // 2

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "][]["
    print(f"Min swaps for '{s1}': {solution.minSwaps(s1)}")
    
    s2 = "]]][[["
    print(f"Min swaps for '{s2}': {solution.minSwaps(s2)}")
