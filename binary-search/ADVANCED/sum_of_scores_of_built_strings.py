# Sum of Scores of Built Strings
# Problem: https://leetcode.com/problems/sum-of-scores-of-built-strings/
# (LC 2223)

class Solution:
    def sumScores(self, s: str) -> int:
        # Score of s_i is length of LCP(s, suffix starting at i).
        # This is exactly the Z-array definition.
        # Sum of Z-array.
        # Z[i] is LCP of s and s[i:].
        
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        total = n # Z[0] is n, usually Z-algo sets Z[0]=0 but problem asks for logic where s matches itself
        
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
            total += z[i]
            
        return total

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumScores("babab")) # Output: 9
