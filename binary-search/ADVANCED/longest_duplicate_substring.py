# Longest Duplicate Substring
# Problem: https://leetcode.com/problems/longest-duplicate-substring/

class Solution:
    def longestDuplicateSubstring(self, s: str) -> str:
        # Binary search on length of the substring.
        # Use rolling hash (Rabin-Karp) to check for duplicates of a given length.
        
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        MOD = 2**63 - 1 # Mersenne prime
        base = 26
        
        def search(L):
            if L == 0: return -1
            
            # Compute hash for first substring of length L
            h = 0
            for i in range(L):
                h = (h * base + nums[i]) % MOD
            
            seen = {h}
            # Constant needed to remove leading character: base^L % MOD
            # Actually base^(L-1)
            aL = pow(base, L, MOD) 
            # Wait, cleaning logic:
            # new_h = (h * base - nums[i] * base^L + nums[i+L]) % MOD
            # where base^L is actually base^L in the formula if we multiply first.
            # Let's use standard sliding window hash update.
            # h_new = ((h_old - nums[i] * (base^(L-1))) * base + nums[i+L])
            
            # Precompute largest power
            pL = pow(base, L - 1, MOD)
            
            for i in range(1, n - L + 1):
                h = (h - nums[i - 1] * pL) % MOD
                h = (h * base + nums[i + L - 1]) % MOD
                if h in seen:
                    return i
                seen.add(h)
            return -1
            
        left, right = 0, n - 1
        start = -1
        max_len = 0
        
        while left <= right:
            mid = (left + right) // 2
            pos = search(mid)
            if pos != -1:
                start = pos
                max_len = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return s[start : start + max_len] if start != -1 else ""

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestDuplicateSubstring("banana")) # Output: "ana"
