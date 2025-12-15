# Meeting Scheduler
# Problem: https://leetcode.com/problems/meeting-scheduler/
# Solution:

from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        
        i, j = 0, 0
        
        while i < len(slots1) and j < len(slots2):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            
            if start + duration <= end:
                return [start, start + duration]
            
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
                
        return []

if __name__ == "__main__":
    solution = Solution()
    
    s1 = [[10,50],[60,120],[140,210]]
    s2 = [[0,15],[60,70]]
    d = 8
    print(f"Meeting schedule: {solution.minAvailableDuration(s1, s2, d)}")
