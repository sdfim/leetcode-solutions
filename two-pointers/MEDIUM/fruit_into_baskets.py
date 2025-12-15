# Fruit Into Baskets
# Problem: https://leetcode.com/problems/fruit-into-baskets/
# Solution:

from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l = 0
        res = 0
        
        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
                
            res = max(res, r - l + 1)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    f1 = [1,2,1]
    print(f"Total fruit {f1}: {solution.totalFruit(f1)}")
    
    f2 = [0,1,2,2]
    print(f"Total fruit {f2}: {solution.totalFruit(f2)}")
