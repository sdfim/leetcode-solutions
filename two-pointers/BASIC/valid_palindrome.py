# Valid Palindrome
# Problem: https://leetcode.com/problems/valid-palindrome/
# Solution:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
        and removing all non-alphanumeric characters, it reads the same forward and backward.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    s1 = "A man, a plan, a canal: Panama"
    print(f"'{s1}' is palindrome: {solution.isPalindrome(s1)}")
    
    s2 = "race a car"
    print(f"'{s2}' is palindrome: {solution.isPalindrome(s2)}")
    
    s3 = " "
    print(f"'{s3}' is palindrome: {solution.isPalindrome(s3)}")
