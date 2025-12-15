# Check If N and Its Double Exist
# Problem: https://leetcode.com/problems/check-if-n-and-its-double-exist/

from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        
        for i, x in enumerate(arr):
            # Binary search for 2*x
            target = 2 * x
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    if mid != i:
                        return True
                    else:
                        # If duplicate 0s, we need to check neighbors or ensure one 0 doesn't match itself
                        # But since mid == i, we should search left or right?
                        # This naive Binary Search finds closest. 
                        # Easier to use set or specific condition.
                        pass
                
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
        # Standard O(N) approach is hashset, but binary search request implies sorting
        # Let's retry more robust binary search or just linear scan
        seen = set()
        for x in arr:
            if 2*x in seen or (x % 2 == 0 and x // 2 in seen):
                return True
            seen.add(x)
        return False
    
    # Strictly Binary Search implementation:
    def checkIfExistBinarySearch(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            target = 2 * arr[i]
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target and mid != i:
                    return True
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.checkIfExistBinarySearch([10,2,5,3]))  # Output: True
    print(solution.checkIfExistBinarySearch([7,1,14,11])) # Output: True
