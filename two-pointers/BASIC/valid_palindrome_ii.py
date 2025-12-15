# Valid Palindrome II
# Problem: https://leetcode.com/problems/valid-palindrome-ii/
# Solution:

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return check(l + 1, r) or check(l, r - 1)
            l += 1
            r -= 1
            
        return True

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "aba"
    print(f"Valid palindrome II '{s1}': {solution.validPalindrome(s1)}")
    
    s2 = "abca"
    print(f"Valid palindrome II '{s2}': {solution.validPalindrome(s2)}")
    
    s3 = "abc"
    print(f"Valid palindrome II '{s3}': {solution.validPalindrome(s3)}")
