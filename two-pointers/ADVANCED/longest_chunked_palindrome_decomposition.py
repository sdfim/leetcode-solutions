# Longest Chunked Palindrome Decomposition
# Problem: https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
# Solution:

class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        res = 0
        l, r = 0, n - 1
        curr_l_str = ""
        curr_r_str = ""
        
        while l <= r:
            curr_l_str += text[l]
            curr_r_str = text[r] + curr_r_str
            
            if curr_l_str == curr_r_str:
                if l == r: # Exact middle overlap of single character
                    res += 1
                else:
                    res += 2
                curr_l_str = ""
                curr_r_str = ""
                
            l += 1
            r -= 1
        
        if curr_l_str != "":
            res += 1
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    text1 = "ghiabcdefhelloadamhelloabcdefghi"
    print(f"Decomposition of '{text1}': {solution.longestDecomposition(text1)}")
    
    text2 = "merchant"
    print(f"Decomposition of '{text2}': {solution.longestDecomposition(text2)}")
