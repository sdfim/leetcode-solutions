# Pancake Sorting
# Problem: https://leetcode.com/problems/pancake-sorting/
# Solution:

from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        
        for x in range(n, 0, -1):
            # Find index of x
            i = -1
            for idx, val in enumerate(arr):
                if val == x:
                    i = idx
                    break
            
            if i == x - 1:
                continue
                
            # Flip valid number to front
            if i != 0:
                res.append(i + 1)
                arr[:i+1] = arr[:i+1][::-1]
                
            # Flip valid number to correct position
            res.append(x)
            arr[:x] = arr[:x][::-1]
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    arr1 = [3,2,4,1]
    print(f"Pancake sort flips for {arr1}: {solution.pancakeSort(arr1)}")
