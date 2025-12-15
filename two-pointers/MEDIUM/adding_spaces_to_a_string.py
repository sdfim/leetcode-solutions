# Adding Spaces to a String
# Problem: https://leetcode.com/problems/adding-spaces-to-a-string/
# Solution:

from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        space_idx = 0
        n = len(spaces)
        
        for i, char in enumerate(s):
            if space_idx < n and i == spaces[space_idx]:
                res.append(' ')
                space_idx += 1
            res.append(char)
            
        return "".join(res)

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "LeetcodeHelpsMeLearn"
    spaces1 = [8,13,15]
    print(f"Adding spaces to '{s1}': '{solution.addSpaces(s1, spaces1)}'")
