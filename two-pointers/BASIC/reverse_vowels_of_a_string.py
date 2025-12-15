# Reverse Vowels of a String
# Problem: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Solution:

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and s_list[l] not in vowels:
                l += 1
            while l < r and s_list[r] not in vowels:
                r -= 1
                
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
            
        return "".join(s_list)

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "hello"
    print(f"Reverse vowels of '{s1}': {solution.reverseVowels(s1)}")
    
    s2 = "leetcode"
    print(f"Reverse vowels of '{s2}': {solution.reverseVowels(s2)}")
