# Smallest Rectangle Enclosing Black Pixels
# Problem: https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # Image is m x n
        m, n = len(image), len(image[0])
        
        # We need to find boundaries: top, bottom, left, right
        # image[i][j] == '1' is black.
        
        # Binary search for top: range [0, x]. Lowest row containing a '1'.
        # To check if row 'r' has a '1', we can iterate.
        # But wait, problem says "black pixels are connected".
        # This implies: simple row check is enough (if it has '1')?
        # Yes. Also due to connectivity, if we project '1's to X axis, they form a range. Same for Y axis.
        
        def has_black_in_row(row):
            return '1' in image[row]
            
        def has_black_in_col(col):
            for i in range(m):
                if image[i][col] == '1':
                    return True
            return False
        
        # Find Top
        # Range [0, x]
        top = x
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if has_black_in_row(mid):
                top = mid
                r = mid - 1
            else:
                l = mid + 1
                
        # Find Bottom
        # Range [x, m-1]
        bottom = x
        l, r = x, m - 1
        while l <= r:
            mid = (l + r) // 2
            if has_black_in_row(mid):
                bottom = mid
                l = mid + 1
            else:
                r = mid - 1
                
        # Find Left
        # Range [0, y]
        left_val = y
        l, r = 0, y
        while l <= r:
            mid = (l + r) // 2
            if has_black_in_col(mid):
                left_val = mid
                r = mid - 1
            else:
                l = mid + 1
        
        # Find Right
        # Range [y, n-1]
        right_val = y
        l, r = y, n - 1
        while l <= r:
            mid = (l + r) // 2
            if has_black_in_col(mid):
                right_val = mid
                l = mid + 1
            else:
                r = mid - 1
                
        return (bottom - top + 1) * (right_val - left_val + 1)

if __name__ == "__main__":
    solution = Solution()
    img = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]]
    print(solution.minArea(img, 0, 2))  # Output: 6
