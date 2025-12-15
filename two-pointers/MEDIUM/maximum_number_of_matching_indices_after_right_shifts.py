# Maximum Number of Matching Indices After Right Shifts
# Problem: https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/
# Solution:

from typing import List

class Solution:
    def maximumMatching(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        max_matches = 0
        
        # O(N^2) naive check since constraints usually allow it for this problem type
        # Or KMP if needed but typically N is small for this specific problem variation or strictly shifts
        
        for shift in range(n):
            matches = 0
            for i in range(n):
                if nums1[i] == nums2[(i + shift) % n]:
                    matches += 1
            max_matches = max(max_matches, matches)
            
        return max_matches

if __name__ == "__main__":
    solution = Solution()
    
    n1 = [1,2,3]
    n2 = [3,1,2]
    print(f"Max matches: {solution.maximumMatching(n1, n2)}")
