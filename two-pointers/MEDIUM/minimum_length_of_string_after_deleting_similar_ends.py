# Minimum Length of String After Deleting Similar Ends
# Problem: https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
# Solution:

class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        
        while l < r and s[l] == s[r]:
            c = s[l]
            while l <= r and s[l] == c:
                l += 1
            while r >= l and s[r] == c:
                r -= 1
                
        return r - l + 1

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "ca"
    print(f"Min length '{s1}': {solution.minimumLength(s1)}")
    
    s2 = "cabaabac"
    print(f"Min length '{s2}': {solution.minimumLength(s2)}")
