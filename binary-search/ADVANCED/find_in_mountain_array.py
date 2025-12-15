# Find in Mountain Array
# Problem: https://leetcode.com/problems/find-in-mountain-array/

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        # 1. Find peak index
        l, r = 0, n - 1
        peak = 0
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        
        # 2. Search in left (increasing) part
        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
                
        # 3. Search in right (decreasing) part
        l, r = peak + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target: # Decreasing slope logic
                l = mid + 1
            else:
                r = mid - 1
                
        return -1

if __name__ == "__main__":
    # Mock MountainArray
    class MountainArrayImpl:
        def __init__(self, arr):
            self.arr = arr
        def get(self, index: int) -> int:
            return self.arr[index]
        def length(self) -> int:
            return len(self.arr)
            
    solution = Solution()
    ma = MountainArrayImpl([1, 2, 3, 4, 5, 3, 1])
    print(solution.findInMountainArray(3, ma)) # Output: 2
