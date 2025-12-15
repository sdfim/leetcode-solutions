# Number of Equal Numbers Blocks
# Problem: https://leetcode.com/problems/number-of-equal-numbers-blocks/

# This problem generally involves a custom class BigArray.
# We will simulate the solution assuming BigArray interface.

class BigArray:
    def __init__(self, elements):
        self.elements = elements
    def at(self, index: int) -> int:
        return self.elements[index]
    def size(self) -> int:
        return len(self.elements)

class Solution:
    def countBlocks(self, nums: BigArray) -> int:
        n = nums.size()
        if n == 0: return 0
        
        blocks = 0
        i = 0
        while i < n:
            blocks += 1
            current_val = nums.at(i)
            
            # Find the end of this block using binary search
            # We want largest index j >= i such that nums.at(j) == current_val
            # Actually we can find FIRST index k > i such that nums.at(k) != current_val
            # Or just jump ahead exponentially?
            # Problem often gives binary search constraint or "BigArray" implies O(log N * blocks).
            
            # Binary search for the change point.
            # Range [i, n-1].
            # Find largest j such that all in [i, j] are current_val.
            # But we can't check 'all'. 
            # Constraint: "all occurrences of a particular value are adjacent".
            # So if nums.at(mid) == current_val, then [i...mid] are all current_val.
            
            left, right = i, n - 1
            end_of_block = i
            
            while left <= right:
                mid = (left + right) // 2
                if nums.at(mid) == current_val:
                    end_of_block = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            i = end_of_block + 1
            
        return blocks

if __name__ == "__main__":
    arr = BigArray([1,1,1,3,9,9,9,2,10,10])
    solution = Solution()
    print(solution.countBlocks(arr)) # 5
