# Maximum Tastiness of Candy Basket
# Problem: https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        
        def check(d):
            # Can we pick k candies with min diff >= d?
            count = 1
            last = price[0]
            for i in range(1, n):
                if price[i] - last >= d:
                    count += 1
                    last = price[i]
            return count >= k
            
        left, right = 0, price[-1] - price[0]
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumTastiness([13,5,1,8,21,2], 3)) # 8
