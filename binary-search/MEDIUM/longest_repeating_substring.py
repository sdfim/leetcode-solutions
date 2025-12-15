# Longest Repeating Substring
# Problem: https://leetcode.com/problems/longest-repeating-substring/

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        
        def search(length):
            seen = set()
            for i in range(n - length + 1):
                sub = s[i : i + length]
                if sub in seen:
                    return True
                seen.add(sub)
            return False
            
        left, right = 1, n - 1
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            if search(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestRepeatingSubstring("abbaba"))  # Output: 2
