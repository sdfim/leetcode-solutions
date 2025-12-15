# Maximum Number of Removable Characters
# Problem: https://leetcode.com/problems/maximum-number-of-removable-characters/
# Solution:

from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(s_arr, p):
            i, j = 0, 0
            while i < len(s_arr) and j < len(p):
                if s_arr[i] == p[j]:
                    j += 1
                i += 1
            return j == len(p)
            
        l, r = 0, len(removable)
        s_list = list(s)
        
        while l <= r:
            mid = (l + r) // 2
            
            # Map removed indices for O(1) checking or just modify a copy
            temp_s = list(s)
            for k in range(mid):
                temp_s[removable[k]] = ''
                
            # Optimized check - reconstruct string without removed chars is slow
            # Instead pass the modified list or use markers
            # Here we just use the list approach but only process valid chars
            # But converting list to string might be slow too.
            # Let's iterate on temp_s directly
            
            # Optimization: 
            # Actually, modifying `temp_s` takes O(N). `isSubsequence` takes O(N).
            # Total binary search is O(N log K).
            
            if isSubsequence([c for c in temp_s if c != ''], p):
                l = mid + 1
            else:
                r = mid - 1
                
        return r

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "abcacb"
    p1 = "ab"
    rem1 = [3,1,0]
    print(f"Max removals s='{s1}', p='{p1}', rem={rem1}: {solution.maximumRemovals(s1, p1, rem1)}")
