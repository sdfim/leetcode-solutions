# Magnetic Force Between Two Balls
# Problem: https://leetcode.com/problems/magnetic-force-between-two-balls/

from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def can_place(force):
            count = 1
            last = position[0]
            for i in range(1, len(position)):
                if position[i] - last >= force:
                    count += 1
                    last = position[i]
            return count >= m
            
        left, right = 1, position[-1] - position[0]
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_place(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistance([1,2,3,4,7], 3))  # Output: 3
