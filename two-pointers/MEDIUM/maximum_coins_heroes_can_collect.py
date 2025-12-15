# Maximum Coins Heroes Can Collect
# Problem: https://leetcode.com/problems/maximum-coins-heroes-can-collect/
# Solution:

from typing import List
import bisect

class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        monster_coins = sorted(zip(monsters, coins))
        monsters = [m for m, c in monster_coins]
        
        prefix_coins = [0] * (len(monster_coins) + 1)
        for i in range(len(monster_coins)):
            prefix_coins[i+1] = prefix_coins[i] + monster_coins[i][1]
            
        res = []
        for h in heroes:
            idx = bisect.bisect_right(monsters, h)
            res.append(prefix_coins[idx])
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    h1 = [1,4,2]
    m1 = [1,1,5,2,3]
    c1 = [2,3,4,5,6]
    print(f"Heroes {h1} coins: {solution.maximumCoins(h1, m1, c1)}")
