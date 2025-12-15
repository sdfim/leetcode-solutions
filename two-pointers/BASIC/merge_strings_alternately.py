# Merge Strings Alternately
# Problem: https://leetcode.com/problems/merge-strings-alternately/
# Solution:

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i, j = 0, 0
        n, m = len(word1), len(word2)
        
        while i < n or j < m:
            if i < n:
                res.append(word1[i])
                i += 1
            if j < m:
                res.append(word2[j])
                j += 1
                
        return "".join(res)

if __name__ == "__main__":
    solution = Solution()
    
    word1 = "abc"
    word2 = "pqr"
    print(f"Merged '{word1}' and '{word2}': {solution.mergeAlternately(word1, word2)}")
