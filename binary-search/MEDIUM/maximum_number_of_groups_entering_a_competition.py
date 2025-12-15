# Maximum Number of Groups Entering a Competition
# Problem: https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # Sort grades.
        # Group 1 size 1, Group 2 size 2, ...
        # Sums will naturally be increasing if we take sorted elements.
        # We just need to find max k such that k*(k+1)/2 <= n.
        # Because we can always form groups of size 1, 2, ..., k with remaining elements added to last group.
        # Wait, strictly less students? No, strict larger size?
        # "sum of grades of the ith group is less than the sum of grades of the (i+1)th group"
        # "number of students in the ith group is less than the number of students in the (i+1)th group"
        # Since grades are positive, if we use more students and larger grades (sorted), sum condition holds.
        # So we just need size condition: 1, 2, 3, ..., k.
        # Total needed: k(k+1)/2 <= n.
        
        n = len(grades)
        # Binary search for k.
        left, right = 1, 1000
        ans = 1
        while left <= right:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumGroups([10,6,12,7,3,5])) # 3
