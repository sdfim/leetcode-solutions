# Is Subsequence
# Problem: https://leetcode.com/problems/is-subsequence/
# Solution:

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "abc"
    t1 = "ahbgdc"
    print(f"Is '{s1}' subsequence of '{t1}': {solution.isSubsequence(s1, t1)}")
    
    s2 = "axc"
    t2 = "ahbgdc"
    print(f"Is '{s2}' subsequence of '{t2}': {solution.isSubsequence(s2, t2)}")
