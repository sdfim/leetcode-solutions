# Watering Plants II
# Problem: https://leetcode.com/problems/watering-plants-ii/
# Solution:

from typing import List

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l, r = 0, len(plants) - 1
        currA, currB = capacityA, capacityB
        recharges = 0
        
        while l <= r:
            if l == r:
                if max(currA, currB) < plants[l]:
                    recharges += 1
                break
                
            if currA < plants[l]:
                recharges += 1
                currA = capacityA
            currA -= plants[l]
            l += 1
            
            if currB < plants[r]:
                recharges += 1
                currB = capacityB
            currB -= plants[r]
            r -= 1
            
        return recharges

if __name__ == "__main__":
    solution = Solution()
    
    plants1 = [2,2,3,3]
    cA = 5
    cB = 5
    print(f"Refills for {plants1}: {solution.minimumRefill(plants1, cA, cB)}")
    
    plants2 = [2,2,3,3]
    cA = 3
    cB = 4
    print(f"Refills for {plants2}: {solution.minimumRefill(plants2, cA, cB)}")
