# Fair Candy Swap
# Problem: https://leetcode.com/problems/fair-candy-swap/

from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        
        # We need sumA - x + y = sumB - y + x
        # 2y - 2x = sumB - sumA
        # y = x + (sumB - sumA) // 2
        
        delta = (sumB - sumA) // 2
        setB = set(bobSizes)
        
        for x in aliceSizes:
            target_y = x + delta
            if target_y in setB:
                return [x, target_y]
        
        return []

if __name__ == "__main__":
    solution = Solution()
    print(solution.fairCandySwap([1,1], [2,2]))  # Output: [1, 2]
