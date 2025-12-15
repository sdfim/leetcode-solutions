# Longest Palindromic Substring
# Problem: https://leetcode.com/problems/longest-palindromic-substring/
# Solution:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Given a string s, return the longest palindromic substring in s.
        """
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # Odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # Even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        return res

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    s1 = "babad"
    print(f"Longest palindrome in '{s1}': {solution.longestPalindrome(s1)}")
    
    s2 = "cbbd"
    print(f"Longest palindrome in '{s2}': {solution.longestPalindrome(s2)}")
