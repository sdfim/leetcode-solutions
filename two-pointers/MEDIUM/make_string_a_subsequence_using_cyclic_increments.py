# Make String a Subsequence Using Cyclic Increments
# Problem: https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/
# Solution:

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        n, m = len(str1), len(str2)
        
        while i < n and j < m:
            c1 = ord(str1[i]) - ord('a')
            c2 = ord(str2[j]) - ord('a')
            
            # Check if same or next char (cyclic)
            if c1 == c2 or (c1 + 1) % 26 == c2:
                j += 1
            i += 1
            
        return j == m

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "abc"
    s2 = "ad"
    print(f"Can make subseq '{s2}' from '{s1}': {solution.canMakeSubsequence(s1, s2)}")
