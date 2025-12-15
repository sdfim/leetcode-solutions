# Longest Common Subpath
# Problem: https://leetcode.com/problems/longest-common-subpath/

from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        # Binary search on length L
        # Rolling hash to verify common subpaths.
        
        base = 100003
        MOD = 2**63 - 1
        
        min_len = min(len(p) for p in paths)
        
        def check(L):
            if L == 0: return True
            
            # Compute hashes for first path
            # Store in set
            common = set()
            
            # Helper to get hashes of length L for a specific path
            def get_hashes(path):
                hashes = set()
                h = 0
                power = pow(base, L - 1, MOD)
                
                for i in range(len(path)):
                    if i < L:
                        h = (h * base + path[i]) % MOD
                    else:
                        h = (h - path[i-L] * power) % MOD
                        h = (h * base + path[i]) % MOD
                    
                    if i >= L - 1:
                        hashes.add(h)
                return hashes

            common = get_hashes(paths[0])
            
            for i in range(1, len(paths)):
                if not common: 
                    return False
                current = get_hashes(paths[i])
                common.intersection_update(current)
            
            return len(common) > 0

        left, right = 0, min_len
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonSubpath(5, [[0,1,2,3,4], [2,3,4], [4,0,1,2,3]]))
    # Output: 2 (path [2,3])
