# Strictly Palindromic Number
# Problem: https://leetcode.com/problems/strictly-palindromic-number/
# Solution:

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # A number n in base (n-2) is always 12.
        # 1*(n-2) + 2 = n
        # '12' is not a palindrome.
        # Thus, for any n >= 4, it's False.
        # The constraint is n >= 4 usually.
        return False

if __name__ == "__main__":
    solution = Solution()
    
    n1 = 9
    print(f"Is {n1} strictly palindromic: {solution.isStrictlyPalindromic(n1)}")
