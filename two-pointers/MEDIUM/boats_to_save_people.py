# Boats to Save People
# Problem: https://leetcode.com/problems/boats-to-save-people/
# Solution:

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            boats += 1
            
        return boats

if __name__ == "__main__":
    solution = Solution()
    
    people1 = [1,2]
    limit1 = 3
    print(f"Boats needed for {people1}, limit {limit1}: {solution.numRescueBoats(people1, limit1)}")
    
    people2 = [3,2,2,1]
    limit2 = 3
    print(f"Boats needed for {people2}, limit {limit2}: {solution.numRescueBoats(people2, limit2)}")
