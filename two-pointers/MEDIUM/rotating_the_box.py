# Rotating the Box
# Problem: https://leetcode.com/problems/rotating-the-box/
# Solution:

from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        res = [['.' for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            # Process each row: simulate gravity to the right
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    empty = j - 1
                elif box[i][j] == '#':
                    box[i][j], box[i][empty] = box[i][empty], box[i][j]
                    empty -= 1
                    
            # Rotate into result (row iBecome col m-1-i)
            for j in range(n):
                res[j][m - 1 - i] = box[i][j]
                
        return res

if __name__ == "__main__":
    solution = Solution()
    
    box1 = [["#",".","#"]]
    print(f"Rotated box {box1}: {solution.rotateTheBox(box1)}")
