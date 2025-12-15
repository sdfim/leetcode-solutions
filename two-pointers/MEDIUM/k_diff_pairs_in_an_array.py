# K-diff Pairs in an Array
# Problem: https://leetcode.com/problems/k-diff-pairs-in-an-array/
# Solution:

from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        count = 0
        
        if k == 0:
            for key, v in c.items():
                if v > 1:
                    count += 1
        else:
            for key, v in c.items():
                if key + k in c:
                    count += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [3,1,4,1,5]
    k1 = 2
    print(f"K-diff pairs in {nums1}, k={k1}: {solution.findPairs(nums1, k1)}")
    
    nums2 = [1,2,3,4,5]
    k2 = 1
    print(f"K-diff pairs in {nums2}, k={k2}: {solution.findPairs(nums2, k2)}")
