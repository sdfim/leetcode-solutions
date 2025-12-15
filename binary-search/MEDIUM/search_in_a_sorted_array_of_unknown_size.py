# Search in a Sorted Array of Unknown Size
# Problem: https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

# """
# This is an interface definition for the ArrayReader.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader:
    def get(self, index: int) -> int:
        pass

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0
            
        # Exponential search to find bounds
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1
            
        # Binary search within bounds
        while left <= right:
            mid = (left + right) // 2
            val = reader.get(mid)
            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

if __name__ == "__main__":
    # Mock
    class MockReader(ArrayReader):
        def __init__(self, arr):
            self.arr = arr
        def get(self, index):
            if index >= len(self.arr):
                return 2**31 - 1
            return self.arr[index]
            
    solution = Solution()
    print(solution.search(MockReader([-1,0,3,5,9,12]), 9))  # Output: 4
