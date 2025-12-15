# Permutation in String
# Problem: https://leetcode.com/problems/permutation-in-string/
# Solution:

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1
                
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            
            l += 1
            
        return matches == 26

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "ab"
    s2 = "eidbaooo"
    print(f"'{s1}' permutation in '{s2}': {solution.checkInclusion(s1, s2)}")
    
    s1 = "ab"
    s2 = "eidboaoo"
    print(f"'{s1}' permutation in '{s2}': {solution.checkInclusion(s1, s2)}")
