# Building Boxes
# Problem: https://leetcode.com/problems/building-boxes/

class Solution:
    def minimumBoxes(self, n: int) -> int:
        # Total boxes for a complete pile of height h:
        # T(h) = sum(i*(i+1)/2 for i in 1..h) = h*(h+1)*(h+2)/6
        
        # Binary search for maximum h such that T(h) <= n
        left, right = 0, 2000 # 2000^3 / 6 > 10^9
        h = 0
        while left <= right:
            mid = (left + right) // 2
            total = mid * (mid + 1) * (mid + 2) // 6
            if total <= n:
                h = mid
                left = mid + 1
            else:
                right = mid - 1
                
        remaining = n - h * (h + 1) * (h + 2) // 6
        if remaining == 0:
            return h * (h + 1) // 2
        
        # Now we need to add 'remaining' boxes.
        # We can add them to the next layer.
        # The k-th added box in the new layer touches k boxes on the floor?
        # No, adding 1 box on floor allows adding 1 (on top of it) + 2 (on top of others) etc?
        # Actually, adding j cells on the floor allows covering j * (j + 1) / 2 volume in the partial layer.
        
        # Find smallest j such that j * (j + 1) / 2 >= remaining
        l_j, r_j = 0, h + 1
        j = 0
        while l_j <= r_j:
            m_j = (l_j + r_j) // 2
            if m_j * (m_j + 1) // 2 >= remaining:
                j = m_j
                r_j = m_j - 1
            else:
                l_j = m_j + 1
                
        return h * (h + 1) // 2 + j

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumBoxes(10)) # Output: 6
