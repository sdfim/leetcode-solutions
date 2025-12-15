# Get Equal Substrings Within Budget
# Problem: https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        
        # Sliding window
        left = 0
        curr_cost = 0
        max_len = 0
        
        for right in range(n):
            curr_cost += costs[right]
            while curr_cost > maxCost:
                curr_cost -= costs[left]
                left += 1
            max_len = max(max_len, right - left + 1)
            
        return max_len

if __name__ == "__main__":
    solution = Solution()
    print(solution.equalSubstring("abcd", "bcdf", 3))  # Output: 3
