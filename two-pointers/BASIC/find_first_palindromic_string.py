# Find First Palindromic String in the Array
# Problem: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
# Solution:

from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""

if __name__ == "__main__":
    solution = Solution()
    
    words1 = ["abc","car","ada","racecar","cool"]
    print(f"First palindrome in {words1}: {solution.firstPalindrome(words1)}")
