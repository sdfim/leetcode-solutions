# Maximum Coins Heroes Can Collect
# Problem: https://leetcode.com/problems/maximum-coins-heroes-can-collect/

from typing import List
import bisect

class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        # Combine monsters and coins
        monster_data = sorted(zip(monsters, coins))
        
        # Extract sorted strengths and prefix sums of coins
        strengths = [m[0] for m in monster_data]
        coin_vals = [m[1] for m in monster_data]
        
        prefix = [0] * (len(coin_vals) + 1)
        for i in range(len(coin_vals)):
            prefix[i+1] = prefix[i] + coin_vals[i]
            
        ans = []
        for h in heroes:
            # Find how many monsters h can beat
            # All m with strength <= h
            idx = bisect.bisect_right(strengths, h)
            ans.append(prefix[idx])
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumCoins([1,4,2], [1,1,5,2,3], [2,3,5,4,3])) # [5,16,10]
