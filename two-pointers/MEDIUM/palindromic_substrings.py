# Palindromic Substrings
# Problem: https://leetcode.com/problems/palindromic-substrings/
# Solution:

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            # Odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                
            # Even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                
        return count

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "abc"
    print(f"Palindromic substrings in '{s1}': {solution.countSubstrings(s1)}")
    
    s2 = "aaa"
    print(f"Palindromic substrings in '{s2}': {solution.countSubstrings(s2)}")
