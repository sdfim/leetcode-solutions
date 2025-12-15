# Reverse Only Letters
# Problem: https://leetcode.com/problems/reverse-only-letters/
# Solution:

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        l, r = 0, len(chars) - 1
        
        while l < r:
            while l < r and not chars[l].isalpha():
                l += 1
            while l < r and not chars[r].isalpha():
                r -= 1
            
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
            
        return "".join(chars)

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "ab-cd"
    print(f"Reverse only letters '{s1}': {solution.reverseOnlyLetters(s1)}")
    
    s2 = "a-bC-dEf-ghIj"
    print(f"Reverse only letters '{s2}': {solution.reverseOnlyLetters(s2)}")
