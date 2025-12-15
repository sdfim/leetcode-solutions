# Find the Index of the Large Integer
# Problem: https://leetcode.com/problems/find-the-index-of-the-large-integer/

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader(object):
    # Compares the sum of arr[l..r] with the sum of arr[x..y]
    # return 1 if sum(arr[l..r]) > sum(arr[x..y])
    # return 0 if sum(arr[l..r]) == sum(arr[x..y])
    # return -1 if sum(arr[l..r]) < sum(arr[x..y])
    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        pass

    # Returns the length of the array
    def length(self) -> int:
        pass

class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left, right = 0, reader.length() - 1
        
        while left < right:
            mid = (right - left + 1) // 2
            # Compare first half vs second half
            # [left, left + mid - 1] vs [left + mid, left + 2*mid - 1]
            # Need to handle odd lengths carefully.
            
            # If length (right - left + 1) is even: split equally
            # If length is odd: include middle element in which part? Or exclude?
            # compareSub allows us to compare ranges.
            
            # Strategy:
            # Split [left, right] into 3 parts if odd? No, API compares 2 ranges.
            # Compare [left, mid_point] vs [mid_point + 1, right]? 
            # Sizes must be equal for meaningful comparison?
            # Problem: "One integer is larger". Sum will deviate.
            # We can pad if needed or just exclude middle if odd.
            # Better strategy: Even length -> compare two halves. 
            # Odd length -> compare first half vs second half excluding last element? Or something.
            
            # Let's try:
            # mid = left + (right - left) // 2
            # If range length is even: compare [left, mid] vs [mid+1, right]
            # If range length is odd: compare [left, mid] vs [mid+1, right] ? Length diff 1.
            # Actually with Reader, if ranges differ in size, sum differs.
            # We must compare Equal ranges.
            
            length = right - left + 1
            half = length // 2
            
            # Compare [left, left + half - 1] and [left + half, left + 2*half - 1]
            res = reader.compareSub(left, left + half - 1, left + half, left + 2*half - 1)
            
            if res == 0:
                # Both halves equal sum. 
                # This implies the larger element is NOT in these 2*half elements.
                # It must be the remaining element if length was odd.
                return right # The only one left out
            elif res == 1:
                # First half larger
                right = left + half - 1
            else:
                # Second half larger
                left = left + half
                right = left + 2*half - 1
                
        return left

if __name__ == "__main__":
    # Mock
    class MockReader(ArrayReader):
        def __init__(self, arr):
            self.arr = arr
        def length(self):
            return len(self.arr)
        def compareSub(self, l, r, x, y):
            s1 = sum(self.arr[l:r+1])
            s2 = sum(self.arr[x:y+1])
            if s1 > s2: return 1
            if s1 == s2: return 0
            return -1
            
    solution = Solution()
    print(solution.getIndex(MockReader([1,1,2,1,1])))  # Output: 2
