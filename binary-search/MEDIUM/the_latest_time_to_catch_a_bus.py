# The Latest Time to Catch a Bus
# Problem: https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        
        p_idx = 0
        last_person_time = -1
        last_bus_has_space = False
        last_bus_arrival = -1
        
        n_p = len(passengers)
        
        for bus_time in buses:
            count = 0
            while count < capacity and p_idx < n_p and passengers[p_idx] <= bus_time:
                last_person_time = passengers[p_idx]
                p_idx += 1
                count += 1
                
            last_bus_has_space = (count < capacity)
            last_bus_arrival = bus_time
            
        # Candidates for best time
        # 1. If last bus has space: last_bus_arrival
        # 2. Else: last_person_time (the one who filled the bus) - 1? No.
        # Actually we look for x such that x is not in passengers, and x puts us in.
        
        best_time = last_bus_arrival if last_bus_has_space else last_person_time
        
        # We process backwards from best_time to find first time NOT occupied.
        # Because we want to arrive at 'best_time' but if taken, simpler to arrive 'best_time - 1'.
        
        # Wait. "Last person who boarded". 
        # If space implies we can arrive at BusTime.
        # If full, we must displace the last person. So arrive at LastPersonTime.
        # But we must be strictly unique.
        
        p_set = set(passengers)
        while best_time in p_set:
            best_time -= 1
            
        return best_time

if __name__ == "__main__":
    solution = Solution()
    print(solution.latestTimeCatchTheBus([10,20], [2,17,18,19], 2)) # 16
