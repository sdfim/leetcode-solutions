# Make Array Empty
# Problem: https://leetcode.com/problems/make-array-empty/

from typing import List

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        # Sort nums based on value, keep original index
        # We must remove elements in increasing order of value.
        # If position of current element < position of previous element, 
        # it means we wrapped around the array once.
        # Operations:
        # Pass 1: remove some.
        # Effectively, we are traversing the array cyclicly.
        # Sum of (n - i) for each wrap?
        
        # Map value -> index
        pos = {val: i for i, val in enumerate(nums)}
        sorted_nums = sorted(nums)
        
        ans = n # We definitely remove n elements (1 op each for removal)
        # Additional ops are "move to end".
        
        # Iterate through sorted order
        # Calculate how many full passes (or skips) needed.
        # Actually logic is:
        # Start at index 0. Target index pos[sorted_nums[0]].
        # Operations += number of available elements between current and target?
        # NO, simpler:
        # If pos[curr] < pos[prev], we started a new pass.
        # Every time we start a new pass, we effectively skipped all REMAINING elements once.
        # So we add (n - i) to answer, where i is number of elements already removed.
        
        # Initial: pass 1.
        # We start conceptually before the array.
        # First element is at index p0.
        # Next element at p1.
        # If p1 < p0, we wrapped around.
        
        # Correction: The logic "If p_curr < p_prev: ans += current_remaining_size"
        # Total operations = n + sum(remaining_size when wrap happens)
        
        curr_remaining = n
        ans = 1 # Initial op for first element
        
        prev_idx = pos[sorted_nums[0]]
        
        for i in range(1, n):
            curr_val = sorted_nums[i]
            curr_idx = pos[curr_val]
            
            if curr_idx < prev_idx:
                # Wrap around occurred
                ans += curr_remaining
                
            ans += 1 # Removing the element itself takes 1 op? 
            # Actually standard formula:
            # If wrap, we pay cost of skipping remaining elements.
            # Removing takes 1 op.
            # If no wrap, we just move forward, cost is just removing?
            # Wait, "move to end" costs ops.
            # Example: [3, 4, -1] -> sorted [-1, 3, 4]. Indices [2, 0, 1].
            # 1. Target -1 (idx 2). Prev virtual -1. 2 > -1. Ops += 1 (remove) + distance?
            # Actually Simulation:
            # Op 1: Remove if first. Else move to end.
            # Sequence of removal indices: p0, p1, p2...
            # If p_next > p_curr: cost is just checking/skipping intervening?
            # No, elements are removed.
            # Accepted logic:
            # ans = N.
            # if pos[i] < pos[i-1]: ans += (N - i)
            # where i is 1-based index of removed element?
            # Let's trace.
            
            # Correct Logic:
            # Base answer is 'n'.
            # Iterate i from 1 to n-1 (0-indexed in sorted).
            # if pos[sorted[i]] < pos[sorted[i-1]]:
            #     ans += (n - i)
            
            prev_idx = curr_idx
            curr_remaining -= 1
            # Wait, remaining decreases. In loop i=1, remaining is n-1.
            # If wrap, add (n-1).
            
        ans = n
        prev_idx = pos[sorted_nums[0]]
        for i in range(1, n):
            curr_idx = pos[sorted_nums[i]]
            if curr_idx < prev_idx:
                ans += (n - i)
            prev_idx = curr_idx
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.countOperationsToEmptyArray([3,4,-1])) # Output: 5
