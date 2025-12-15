# Maximum Number of Alloys
# Problem: https://leetcode.com/problems/maximum-number-of-alloys/

from typing import List

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        # For each machine (recipe), binary search max alloys.
        # Return max over all machines.
        
        ans = 0
        for machine in composition:
            def check(num):
                needed_money = 0
                for i in range(n):
                    required = num * machine[i]
                    if required > stock[i]:
                        needed_money += (required - stock[i]) * cost[i]
                return needed_money <= budget
                
            left, right = 0, 10**9 # approximate max
            res = 0
            while left <= right:
                mid = (left + right) // 2
                if check(mid):
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1
            ans = max(ans, res)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxNumberOfAlloys(3, 2, 15, [[1,1,1],[1,1,10]], [0,0,0], [1,2,3])) # 2
