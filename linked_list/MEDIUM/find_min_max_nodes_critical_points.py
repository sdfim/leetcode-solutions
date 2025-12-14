# Find the Min & Max Nodes Between Critical Points
# Problem: https://leetcode.com/problems/find-the-min-max-nodes-between-critical-points/
# Solution:

from typing import Optional, List
from linked_list.utils import ListNode, create_linked_list

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, current = None, head
        index, critical_points = 0, []

        while current and current.next:
            if prev and ((current.val > prev.val and current.val > current.next.val) or
                         (current.val < prev.val and current.val < current.next.val)):
                critical_points.append(index)
            prev, current = current, current.next
            index += 1

        if len(critical_points) < 2:
            return [-1, -1]

        min_distance = min(b - a for a, b in zip(critical_points, critical_points[1:]))
        max_distance = critical_points[-1] - critical_points[0]
        return [min_distance, max_distance]

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([1, 3, 2, 2, 3, 2, 2, 2, 7])
    solution = Solution()
    result = solution.nodesBetweenCriticalPoints(head)
    print(f"Min and Max distances: {result}")
