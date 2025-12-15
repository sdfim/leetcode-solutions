# Intersection of Three Sorted Arrays
# Problem: https://leetcode.com/problems/intersection-of-three-sorted-arrays/

from typing import List

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        p1, p2, p3 = 0, 0, 0
        res = []
        
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                res.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                max_val = max(arr1[p1], arr2[p2], arr3[p3])
                if arr1[p1] < max_val: p1 += 1
                if arr2[p2] < max_val: p2 += 1
                if arr3[p3] < max_val: p3 += 1
        
        return res

if __name__ == "__main__":
    solution = Solution()
    arr1 = [1,2,3,4,5]
    arr2 = [1,2,5,7,9]
    arr3 = [1,3,4,5,8]
    print(solution.arraysIntersection(arr1, arr2, arr3))  # Output: [1, 5]
