# Maximize the Minimum Powered City
# Problem: https://leetcode.com/problems/maximize-the-minimum-powered-city/

from typing import List
import pprint

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        
        # Calculate initial power for each city using sliding window
        initial_power = [0] * n
        window_sum = sum(stations[:r]) # sum of 0 to r-1
        # city 0 covered by [0, r]
        # city i covered by [max(0, i-r), min(n-1, i+r)]
        
        # Proper initialization
        # Sliding window range [left, right] for city i
        # For city 0, range is [0, r].
        current_sum = 0
        for i in range(min(n, r + 1)):
            current_sum += stations[i]
        initial_power[0] = current_sum
        
        for i in range(1, n):
            # Remove i - r - 1 if it was in window
            if i - r - 1 >= 0:
                current_sum -= stations[i - r - 1]
            # Add i + r if it is in range
            if i + r < n:
                current_sum += stations[i + r]
            initial_power[i] = current_sum
            
        def check(min_val):
            needed = 0
            # Difference array (or queue) to track added stations
            added = [0] * n
            curr_added = 0
            
            nonlocal n, r
            
            for i in range(n):
                # Remove effect of stations added at i - r - 1 (out of range now? No)
                # Range of effect for station at X is [X-r, X+r].
                # So if we are at city i, stations added at index X contribute if i <= X + r => X >= i - r.
                # Also i >= X - r => X <= i + r.
                # When moving from i to i+1, usually tracking window sum is easier.
                
                # Logic: We greedy add stations at min(n-1, i+r) to cover i and max future.
                # The effect starts at i and ends at min(n-1, i+r) + r = i + 2*r.
                # Actually, standard greedy interval coverage.
                pass
            
            # Restart refined greedy
            # Use 'diff' array to track 'boost'
            diff = [0] * (n + 1)
            current_boost = 0
            count = 0
            
            for i in range(n):
                current_boost += diff[i]
                power = initial_power[i] + current_boost
                
                if power < min_val:
                    deficit = min_val - power
                    count += deficit
                    if count > k:
                        return False
                    
                    # We add 'deficit' stations at min(n-1, i+r)
                    # These stations cover [pos-r, pos+r].
                    # Since pos >= i, i is covered.
                    # Coverage ends at pos + r.
                    # So boost applies until pos + r. Next index (pos + r + 1) loses boost.
                    
                    pos = min(n - 1, i + r)
                    current_boost += deficit
                    if pos + r + 1 < n:
                        diff[pos + r + 1] -= deficit
                        
            return True

        left, right = 0, sum(stations) + k
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxPower([1,2,4,5,0], 1, 2)) # Output: 5
