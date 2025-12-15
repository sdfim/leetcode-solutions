# Append Characters to String to Make Subsequence
# Problem: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
# Solution:

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
            
        return len(t) - j

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "coaching"
    t1 = "coding"
    print(f"Append chars to make subseq s='{s1}', t='{t1}': {solution.appendCharacters(s1, t1)}")
