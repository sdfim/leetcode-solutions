# Divide Chocolate
# Problem: https://leetcode.com/problems/divide-chocolate/

from typing import List

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # We need to divide into k + 1 pieces.
        # Maximize the minimum sweetness of any piece.
        
        def can_split(min_val):
            count = 0
            current_sum = 0
            for s in sweetness:
                current_sum += s
                if current_sum >= min_val:
                    count += 1
                    current_sum = 0
            return count >= k + 1
            
        left, right = 1, sum(sweetness) // (k + 1)
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_split(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximizeSweetness([1,2,3,4,5,6,7,8,9], 5)) # Output: 6
