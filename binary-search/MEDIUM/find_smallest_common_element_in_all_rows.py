# Find Smallest Common Element in All Rows
# Problem: https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

from typing import List
import bisect

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # Check elements of first row against all other rows
        # For small matricies (500x500), O(R*C log C) or O(R*C) is fine.
        
        # Intersection approach (O(total elements))
        common = set(mat[0])
        for i in range(1, len(mat)):
            common &= set(mat[i]) # Set intersection is efficient
            if not common:
                return -1
                
        if common:
            return min(common)
        return -1
        
        # Binary Search approach:
        # for val in mat[0]:
        #    found_in_all = True
        #    for i in range(1, len(mat)):
        #        if not binary_search(mat[i], val):
        #             found_in_all = False; break
        #    if found_in_all: return val

if __name__ == "__main__":
    solution = Solution()
    mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
    print(solution.smallestCommonElement(mat))  # Output: 5
