# Longest Word in Dictionary through Deleting
# Problem: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
# Solution:

from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # Sort by length (descending) then lexicographical (ascending)
        dictionary.sort(key=lambda x: (-len(x), x))
        
        for word in dictionary:
            i = 0
            for char in s:
                if i < len(word) and char == word[i]:
                    i += 1
            
            if i == len(word):
                return word
                
        return ""

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "abpcplea"
    d1 = ["ale","apple","monkey","plea"]
    print(f"Longest word in {d1} from '{s1}': {solution.findLongestWord(s1, d1)}")
