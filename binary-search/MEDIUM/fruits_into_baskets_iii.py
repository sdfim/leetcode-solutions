# Fruit Into Baskets III
# Problem: Assuming variation of Fruit Into Baskets with K baskets.

from typing import List
import collections

class Solution:
    def totalFruit(self, fruits: List[int], k: int = 3) -> int:
        # Standard Fruit Into Baskets is k=2.
        # This implementation supports variable k.
        
        count = collections.defaultdict(int)
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            count[fruits[right]] += 1
            
            while len(count) > k:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
                
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits

if __name__ == "__main__":
    solution = Solution()
    print(solution.totalFruit([1,2,3,2,2], 2)) # 4
