# Online Election
# Problem: https://leetcode.com/problems/online-election/

from typing import List
import bisect
import collections

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        count = collections.defaultdict(int)
        leader = -1
        
        for p in persons:
            count[p] += 1
            if leader == -1 or count[p] >= count[leader]:
                leader = p
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        # Find time <= t
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]

if __name__ == "__main__":
    obj = TopVotedCandidate([0,1,1,0,0,1,0], [0,5,10,15,20,25,30])
    print(obj.q(3))  # Output: 0
    print(obj.q(12)) # Output: 1
