# Partition Array Into Two Arrays to Minimize Sum Difference
# Problem: https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

from typing import List
import bisect

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total_sum = sum(nums)
        target = total_sum // 2
        
        left_part = nums[:n]
        right_part = nums[n:]
        
        # Generate all subset sums for a part, organized by size (count of elements)
        def get_sums(arr):
            # Returns dict: size -> sorted list of sums
            sums = {0: [0]}
            for num in arr:
                # Iterate backwards to avoid using same element twice in one update?
                # Using a new dict is safer
                new_sums = {}
                for count, val_list in sums.items():
                    # Keep existing
                    if count not in new_sums: new_sums[count] = []
                    new_sums[count].extend(val_list)
                    
                    # Add current num
                    next_count = count + 1
                    if next_count not in new_sums: new_sums[next_count] = []
                    for val in val_list:
                        new_sums[next_count].append(val + num)
                sums = new_sums
            
            for k in sums:
                sums[k].sort()
            return sums
            
        left_sums = get_sums(left_part)
        right_sums = get_sums(right_part)
        
        min_diff = abs(total_sum - 2 * left_sums[0][0]) # Init with 0 elements from left (so sum 0) and 0 from right? No, need n elements total.
        # Actually need exactly n elements.
        # If we pick k from left, we need n-k from right.
        
        # Initialize min_diff properly
        min_diff = float('inf')
        
        for k in range(n + 1):
            if k in left_sums and (n - k) in right_sums:
                ls = left_sums[k]
                rs = right_sums[n - k]
                
                # For each s1 in ls, find s2 in rs such that s1 + s2 ≈ target
                for s1 in ls:
                    needed = target - s1
                    idx = bisect.bisect_left(rs, needed)
                    
                    # Check idx and idx-1
                    if idx < len(rs):
                        s2 = rs[idx]
                        current_sum = s1 + s2
                        diff = abs(total_sum - 2 * current_sum)
                        min_diff = min(min_diff, diff)
                        
                    if idx > 0:
                        s2 = rs[idx - 1]
                        current_sum = s1 + s2
                        diff = abs(total_sum - 2 * current_sum)
                        min_diff = min(min_diff, diff)
                        
        return min_diff

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDifference([3,9,7,3])) # Output: 2
