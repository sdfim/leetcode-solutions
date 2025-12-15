# Longest Valid Obstacle Course at Each Position
# Problem: https://leetcode.com/problems/longest-valid-obstacle-course-at-each-position/

from typing import List
import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # We need longest non-decreasing subsequence ending at each index i, including obstacles[i].
        # Standard LIS greedy approach.
        # Maintain `lis` array where `lis[k]` is the smallest tail of a non-decreasing subsequence of length k+1.
        # Since we want non-decreasing (val >= prev), we use `bisect_right`.
        
        lis = []
        ans = []
        
        for val in obstacles:
            # Find insertion position
            # bisect_right returns index where all elements to left are <= val.
            # So elements at idx are > val.
            # We can extend a sequence of length `idx` ending with <= val.
            # So new length is idx + 1.
            idx = bisect.bisect_right(lis, val)
            if idx == len(lis):
                lis.append(val)
            else:
                lis[idx] = val
            ans.append(idx + 1)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestObstacleCourseAtEachPosition([1,2,3,2])) # Output: [1,2,3,3]
