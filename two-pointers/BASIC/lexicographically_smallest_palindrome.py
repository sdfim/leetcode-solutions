# Lexicographically Smallest Palindrome
# Problem: https://leetcode.com/problems/lexicographically-smallest-palindrome/
# Solution:

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)
        l, r = 0, len(s) - 1
        
        while l < r:
            if s_list[l] != s_list[r]:
                min_char = min(s_list[l], s_list[r])
                s_list[l] = min_char
                s_list[r] = min_char
            l += 1
            r -= 1
            
        return "".join(s_list)

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "egcfe"
    print(f"Smallest palindrome from '{s1}': {solution.makeSmallestPalindrome(s1)}")
    
    s2 = "abcd"
    print(f"Smallest palindrome from '{s2}': {solution.makeSmallestPalindrome(s2)}")
