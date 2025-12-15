# Count Good Triplets in an Array
# Problem: https://leetcode.com/problems/count-good-triplets-in-an-array/

from typing import List

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # Remap nums1 to 0..n-1
        # Let pos[v] be position of v in nums2
        # We want i < j < k in nums1 such that pos[nums1[i]] < pos[nums1[j]] < pos[nums1[k]]
        
        # Let arr = [pos[v] for v in nums1].
        # We need to find increasing subsequences of length 3 in arr.
        
        pos_in_nums2 = {val: i for i, val in enumerate(nums2)}
        arr = [pos_in_nums2[x] for x in nums1]
        
        # For each element arr[j], count elements to left smaller than arr[j] (L_smaller)
        # and elements to right larger than arr[j] (R_larger).
        # ans = sum(L_smaller * R_larger)
        
        class BIT:
            def __init__(self, size):
                self.tree = [0] * (size + 1)
            def update(self, i, delta):
                i += 1 # 1-based
                while i < len(self.tree):
                    self.tree[i] += delta
                    i += i & (-i)
            def query(self, i):
                i += 1
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & (-i)
                return s
        
        bit_left = BIT(n)
        left_smaller = [0] * n
        for i in range(n):
            val = arr[i]
            left_smaller[i] = bit_left.query(val - 1)
            bit_left.update(val, 1)
            
        bit_right = BIT(n)
        right_larger = [0] * n
        for i in range(n - 1, -1, -1):
            val = arr[i]
            # Total elements seen so far to right is (n - 1 - i)
            # Smaller to right is bit_right.query(val - 1)
            # Larger to right = Total_seen - Smaller_right
            total_seen = (n - 1 - i)
            smaller_right = bit_right.query(val - 1)
            right_larger[i] = total_seen - smaller_right
            bit_right.update(val, 1)
            
        ans = 0
        for i in range(n):
            ans += left_smaller[i] * right_larger[i]
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.goodTriplets([2,0,1,3], [0,1,2,3])) # Output: 1
