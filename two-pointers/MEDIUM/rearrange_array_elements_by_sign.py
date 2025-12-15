# Rearrange Array Elements by Sign
# Problem: https://leetcode.com/problems/rearrange-array-elements-by-sign/
# Solution:

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for x in nums:
            if x > 0:
                pos.append(x)
            else:
                neg.append(x)
                
        res = []
        for p, n in zip(pos, neg):
            res.append(p)
            res.append(n)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [3,1,-2,-5,2,-4]
    print(f"Rearranged {nums1}: {solution.rearrangeArray(nums1)}")
