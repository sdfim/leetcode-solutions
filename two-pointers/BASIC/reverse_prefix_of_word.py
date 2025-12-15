# Reverse Prefix of Word
# Problem: https://leetcode.com/problems/reverse-prefix-of-word/
# Solution:

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
            
        return word[:idx+1][::-1] + word[idx+1:]

if __name__ == "__main__":
    solution = Solution()
    
    word1 = "abcdefd"
    ch1 = "d"
    print(f"Reverse prefix of '{word1}' at '{ch1}': {solution.reversePrefix(word1, ch1)}")
