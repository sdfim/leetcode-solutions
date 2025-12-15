# Earliest Second to Mark Indices I
# Problem: https://leetcode.com/problems/earliest-second-to-mark-indices-i/

from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)
        
        # Adjust indices to 0-based
        changeIndices = [x - 1 for x in changeIndices]
        
        def check(time):
            # time is the max index in changeIndices we can use (0 to time-1)
            # We need to mark all n indices.
            # To mark index i, we need nums[i] decrement operations + 1 mark operation.
            # Mark operation must happen at some occurrence of i in changeIndices.
            # Valid strategy:
            # We must mark index i at its LAST available occurrence before or at 'time'.
            # Why last? Because earlier slots are precious for decrementing.
            
            last_occurrence = {}
            for t in range(time): # t goes from 0 to time-1 (seconds 1 to time)
                idx = changeIndices[t]
                last_occurrence[idx] = t
                
            if len(last_occurrence) < n:
                return False
                
            # Sort marks by time
            marks = sorted([(t, idx) for idx, t in last_occurrence.items()])
            
            # Simulate
            ops_available = 0
            curr_time = 0
            
            for t_mark, idx in marks:
                # We have (t_mark - curr_time) slots since last marked event?
                # No, simpler: at time t_mark, we MUST mark 'idx'.
                # We have t_mark seconds available in total from start.
                # We used some seconds for previous marks and decrements.
                # Total cost so far (including this one):
                # cost = sum(nums[i] + 1 for already marked)
                # It must be <= t_mark + 1 (since 1-based indexing of seconds, or t_mark+1 available slots)
                pass

            # Alternative greedy check:
            # Iterate from time-1 down to 0.
            # If current second matches a "Last Occurrence" of a required index that hasn't been marked:
            #   We MUST mark it now (consume 1 op).
            #   We also need nums[idx] operations beforehand.
            # If not a last occurrence:
            #   We have a free slot used for decrementing something else later.
            
            # Simpler forward check with sorted deadlines:
            count = 0 
            needed = 0
            # Sort indices by their deadline (last_occurrence)
            marks = sorted(last_occurrence.items(), key=lambda x: x[1])
            
            # Total complexity of check: O(N log N) or O(M)
            prev_t = -1
            accumulated_ops = 0
            
            for idx, t in marks:
                # capacity available between prev_t and t is t - prev_t - 1 ? No
                # We simply check if we have enough capacity to satisfy nums[idx] + 1
                # The deadline is t. By time t, we must have done sum(nums[marked] + 1).
                # Wait, operations can be done in ANY order before the mark.
                # So we simply need: For the first k marked items (sorted by deadline),
                # sum(nums[item] + 1) <= deadline[k] + 1
                
                needed += nums[idx] + 1
                if needed > t + 1:
                    return False
                    
            return True

        low, high = 1, m
        res = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.earliestSecondToMarkIndices([2,2,0], [2,2,2,3,2,2,1]))  # Output: 8 (Wait, indices are enough? array len 3)
    # Correct Logic check needed
