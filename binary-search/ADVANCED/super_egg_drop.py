# Super Egg Drop
# Problem: https://leetcode.com/problems/super-egg-drop/

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[m][k] - max floors we can check with m moves and k eggs.
        # dp[m][k] = dp[m-1][k-1] (egg breaks) + dp[m-1][k] (egg survives) + 1
        
        dp = [0] * (k + 1)
        m = 0
        while dp[k] < n:
            m += 1
            for x in range(k, 0, -1):
                dp[x] = dp[x-1] + dp[x] + 1
        return m

if __name__ == "__main__":
    solution = Solution()
    print(solution.superEggDrop(2, 6))  # Output: 3
