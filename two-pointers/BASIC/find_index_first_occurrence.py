# Find the Index of the First Occurrence in a String
# Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Solution:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack.
        """
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
                
        return -1

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    haystack1 = "sadbutsad"
    needle1 = "sad"
    print(f"Index of '{needle1}' in '{haystack1}': {solution.strStr(haystack1, needle1)}")
    
    haystack2 = "leetcode"
    needle2 = "leeto"
    print(f"Index of '{needle2}' in '{haystack2}': {solution.strStr(haystack2, needle2)}")
