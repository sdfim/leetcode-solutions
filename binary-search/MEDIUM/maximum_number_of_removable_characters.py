# Maximum Number of Removable Characters
# Problem: https://leetcode.com/problems/maximum-number-of-removable-characters/

from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # Binary search k.
        # Check if p is subsequence of s after removing removable[:k].
        
        def is_subseq(s_chars, p_chars):
            i, j = 0, 0
            n, m = len(s_chars), len(p_chars)
            while i < n and j < m:
                if s_chars[i] == p_chars[j]:
                    j += 1
                i += 1
            return j == m

        def check(k):
            removed = set(removable[:k])
            # Construct s without removed
            # Using list for O(N) check
            s_filtered = []
            for i, c in enumerate(s):
                if i not in removed:
                    s_filtered.append(c)
            return is_subseq(s_filtered, p)

        left, right = 0, len(removable)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumRemovals("abcacb", "ab", [3,1,0])) # 2
