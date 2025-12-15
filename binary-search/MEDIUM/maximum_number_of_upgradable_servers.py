# Maximum Number of Upgradable Servers
# Problem: https://leetcode.com/problems/maximum-number-of-upgradable-servers/

from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        ans = []
        n = len(count)
        
        for i in range(n):
            # Formula derivation:
            # Let x be number of upgrades.
            # 0 <= x <= count[i]
            # Cost <= Money available.
            # Money available = money[i] + (count[i] - x) * sell[i].
            # Cost = x * upgrade[i].
            # x * upgrade[i] <= money[i] + count[i]*sell[i] - x*sell[i]
            # x * (upgrade[i] + sell[i]) <= money[i] + count[i]*sell[i]
            # x <= (money[i] + count[i]*sell[i]) / (upgrade[i] + sell[i])
            
            numerator = money[i] + count[i] * sell[i]
            denominator = upgrade[i] + sell[i]
            
            x = numerator // denominator
            
            # Constraint: cannot upgrade more than count[i]
            ans.append(min(int(x), count[i]))
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxUpgrades([4], [3], [4], [8])) # [3]
