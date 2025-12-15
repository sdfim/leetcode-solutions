# Separate Squares I
# Problem: https://leetcode.com/problems/separate-squares-i/

from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # squares[i] = [x, y, l]
        # Total area
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2.0
        
        # Range of Y
        min_y = min(y for _, y, _ in squares)
        max_y = max(y + l for _, y, l in squares)
        
        def get_area_below(h):
            area = 0.0
            for _, y, l in squares:
                if y >= h:
                    continue
                elif y + l <= h:
                    area += l * l
                else:
                    # Square intersects line h
                    # Part below is h - y height
                    area += (h - y) * l
            return area
            
        low, high = min_y, max_y
        for _ in range(60): # Precision
            mid = (low + high) / 2
            if get_area_below(mid) < target:
                low = mid
            else:
                high = mid
                
        return high

if __name__ == "__main__":
    solution = Solution()
    print(f"{solution.separateSquares([[0,0,1],[2,2,1]]):.5f}") # 1.00000
