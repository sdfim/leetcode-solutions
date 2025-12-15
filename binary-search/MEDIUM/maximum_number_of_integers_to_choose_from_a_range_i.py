# Maximum Number of Integers to Choose From a Range I
# Problem: https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # This is a greedy problem, but can we binary search the COUNT k?
        # If we pick k elements, we should pick the k smallest non-banned.
        # Greedy is simple enough: 1, 2, 3... skip banned.
        # Since n is small (10^4), greedy is O(n).
        # We'll use a set for banned.
        
        banned_set = set(banned)
        current_sum = 0
        count = 0
        for i in range(1, n + 1):
            if i in banned_set:
                continue
            if current_sum + i <= maxSum:
                current_sum += i
                count += 1
            else:
                break
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxCount([1,6,5], 5, 6)) # 2
