# Maximum Matching of Players With Trainers
# Problem: https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
# Solution:

from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        i, j = 0, 0
        matches = 0
        
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                matches += 1
                i += 1
                j += 1
            else:
                j += 1
                
        return matches

if __name__ == "__main__":
    solution = Solution()
    
    p1 = [4,7,9]
    t1 = [8,2,5,8]
    print(f"Matches for {p1}, {t1}: {solution.matchPlayersAndTrainers(p1, t1)}")
