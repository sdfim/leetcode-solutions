# Count the Number of K-Big Indices
# Problem: https://leetcode.com/problems/count-the-number-of-k-big-indices/

from typing import List

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Use BIT to count smaller elements
        # Coordinate compression isn't strictly needed if range is small, 
        # but nums can be large. Let's compress.
        
        sorted_nums = sorted(list(set(nums)))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_nums)}
        m = len(sorted_nums)
        
        # BIT class
        class BIT:
            def __init__(self, size):
                self.tree = [0] * (size + 1)
            def update(self, i, delta):
                while i < len(self.tree):
                    self.tree[i] += delta
                    i += i & (-i)
            def query(self, i):
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & (-i)
                return s
                
        # Left Pass
        bit_left = BIT(m)
        is_left_valid = [False] * n
        
        for i in range(n):
            rank = rank_map[nums[i]]
            # Count elements strictly smaller than nums[i]
            count = bit_left.query(rank - 1)
            if count >= k:
                is_left_valid[i] = True
            bit_left.update(rank, 1)
            
        # Right Pass
        bit_right = BIT(m)
        ans = 0
        
        for i in range(n - 1, -1, -1):
            rank = rank_map[nums[i]]
            count = bit_right.query(rank - 1)
            if count >= k and is_left_valid[i]:
                ans += 1
            bit_right.update(rank, 1)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.kBigIndices([2,3,6,5,2,3], 2)) # Output: 2
