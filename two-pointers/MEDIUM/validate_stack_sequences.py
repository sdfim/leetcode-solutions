# Validate Stack Sequences
# Problem: https://leetcode.com/problems/validate-stack-sequences/
# Solution: (Though mostly stack, can be seen as two pointers on pushed/popped)

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                
        return j == len(popped)

if __name__ == "__main__":
    solution = Solution()
    
    pushed1 = [1,2,3,4,5]
    popped1 = [4,5,3,2,1]
    print(f"Valid stack seq pushed={pushed1}, popped={popped1}: {solution.validateStackSequences(pushed1, popped1)}")
