# Largest Merge Of Two Strings
# Problem: https://leetcode.com/problems/largest-merge-of-two-strings/
# Solution:

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = []
        i, j = 0, 0
        
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1
        
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)

if __name__ == "__main__":
    solution = Solution()
    
    w1 = "cabaa"
    w2 = "bcaaa"
    print(f"Largest merge '{w1}', '{w2}': {solution.largestMerge(w1, w2)}")
    
    w1 = "abcabc"
    w2 = "abdcaba"
    print(f"Largest merge '{w1}', '{w2}': {solution.largestMerge(w1, w2)}")
