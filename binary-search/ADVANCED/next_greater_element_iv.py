# Next Greater Element IV
# Problem: https://leetcode.com/problems/next-greater-element-iv/

from typing import List
import heapq

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        
        # Stack s1 stores indices j awaiting their FIRST greater element.
        # s1 will be monotonic decreasing (values nums[j]).
        s1 = []
        
        # Min-heap pq stores (value, index) for indices awaiting their SECOND greater element.
        # These indices have already found their first greater element.
        pq = []
        
        for i, x in enumerate(nums):
            # 1. Process pq: IF current x is greater than val in pq, 
            # then x is the SECOND greater element for that index.
            while pq and pq[0][0] < x:
                val, idx = heapq.heappop(pq)
                ans[idx] = x
                
            # 2. Process s1: If current x is greater than nums[s1[-1]], 
            # then x is the FIRST greater element for s1[-1].
            # Move s1[-1] to pq.
            
            temp_move = []
            while s1 and nums[s1[-1]] < x:
                idx = s1.pop()
                temp_move.append(idx)
            
            # Add to pq
            for idx in temp_move:
                heapq.heappush(pq, (nums[idx], idx))
                
            # 3. Add current index to s1
            s1.append(i)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.secondGreaterElement([2,4,0,9,6])) # Output: [9,6,6,-1,-1]
