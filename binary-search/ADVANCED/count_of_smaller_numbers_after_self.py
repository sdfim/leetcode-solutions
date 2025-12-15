# Count of Smaller Numbers After Self
# Problem: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from typing import List
import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Using sorted list (or BIT/Fenwick)
        # O(N log N)
        sorted_list = []
        res = []
        
        for n in reversed(nums):
            idx = bisect.bisect_left(sorted_list, n)
            res.append(idx)
            bisect.insort(sorted_list, n)
            
        return res[::-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.countSmaller([5,2,6,1]))  # Output: [2,1,1,0]
