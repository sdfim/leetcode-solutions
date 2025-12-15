# Valid Palindrome IV
# Problem: https://leetcode.com/problems/valid-palindrome-iv/
# Solution:

class Solution:
    def makePalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        diff = 0
        
        while l < r:
            if s[l] != s[r]:
                diff += 1
            l += 1
            r -= 1
            
        return diff <= 2

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "abcdba"
    print(f"Can make {s1} palindrome with <= 2 edits: {solution.makePalindrome(s1)}")
    
    s2 = "aa"
    print(f"Can make {s2} palindrome with <= 2 edits: {solution.makePalindrome(s2)}")
