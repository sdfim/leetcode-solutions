# Maximum Points Inside the Square
# Problem: https://leetcode.com/problems/maximum-points-inside-the-square/

from typing import List
import collections

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        # Distance metric: max(|x|, |y|)
        # Organize points by distance
        data = []
        for (x, y), char in zip(points, s):
            dist = max(abs(x), abs(y))
            data.append((dist, char))
            
        data.sort()
        
        seen_chars = set()
        count = 0
        
        # Iterate through points
        # Be careful with points at SAME distance.
        # We need to process all points at distance 'd' together?
        # No, if a point at distance d is invalid, ALL points at >= d are invalid?
        # Wait, if we choose square size D. We include all points with dist < D (strictly inside?)
        # Problem: "inside or on the border". So dist <= D.
        # If we pick D, all points <= D are in.
        # Valid if no duplicates in valid set.
        # We want max points.
        
        # Let 'bad_dist' be the minimum distance 'd' where a duplicate occurs.
        # If we have two 'a' chars at dist1 and dist2 (dist1 <= dist2).
        # We can include 'a' at dist1. But if we include dist2, invalid.
        # So we cannot pick size >= dist2.
        # We perform limit = min(second occurrence of any char).
        # And any point with dist < limit is included.
        # And if limit is exactly dist of a point, can we include points WITH that dist?
        # Only if that point is NOT the duplicate and doesn't conflict with another at same dist.
        # Actually easier: track "min dist of second occurrence".
        
        min_second_dist = float('inf')
        seen = {} # char -> first dist
        
        for d, char in data:
            if char in seen:
                # This is second (or later) occurrence.
                min_second_dist = min(min_second_dist, d)
            else:
                seen[char] = d
                
        # Count points with dist < min_second_dist
        ans = 0
        for d, char in data:
            if d < min_second_dist:
                ans += 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxPointsInsideSquare([[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], "abdca")) # 2
