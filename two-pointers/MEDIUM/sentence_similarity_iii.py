# Sentence Similarity III
# Problem: https://leetcode.com/problems/sentence-similarity-iii/
# Solution:

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        if len(words1) < len(words2):
            words1, words2 = words2, words1
            
        l, r = 0, 0
        n1, n2 = len(words1), len(words2)
        
        while l < n2 and words1[l] == words2[l]:
            l += 1
            
        while r < n2 and words1[n1 - 1 - r] == words2[n2 - 1 - r]:
            r += 1
            
        return l + r >= n2

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "My name is Haley"
    s2 = "My Haley"
    print(f"Similar '{s1}', '{s2}': {solution.areSentencesSimilar(s1, s2)}")
    
    s1 = "of"
    s2 = "A lot of words"
    print(f"Similar '{s1}', '{s2}': {solution.areSentencesSimilar(s1, s2)}")
