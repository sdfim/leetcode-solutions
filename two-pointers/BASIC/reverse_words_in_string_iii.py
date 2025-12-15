# Reverse Words in a String III
# Problem: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Solution:

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversed_words = [word[::-1] for word in words]
        return " ".join(reversed_words)

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "Let's take LeetCode contest"
    print(f"Reverse words III: '{solution.reverseWords(s1)}'")
