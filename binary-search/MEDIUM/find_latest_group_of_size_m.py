# Find Latest Group of Size M
# Problem: https://leetcode.com/problems/find-latest-group-of-size-m/

from typing import List

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # Simulation with boundary tracking. O(N).
        # We need "Binary Search" approach?
        # Maybe reverse simulation?
        
        n = len(arr)
        if m == n:
            return n
            
        length = [0] * (n + 2)
        count = [0] * (n + 1) # count[len] = frequency of groups of length len
        res = -1
        
        for step, i in enumerate(arr):
            left = length[i - 1]
            right = length[i + 1]
            
            new_len = left + right + 1
            length[i] = new_len
            
            # Update boundaries
            length[i - left] = new_len
            length[i + right] = new_len
            
            # Update counts
            count[left] -= 1
            count[right] -= 1
            count[new_len] += 1
            
            if count[m] > 0:
                res = step + 1
                
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.findLatestStep([3,5,1,2,4], 1))  # Output: 4
