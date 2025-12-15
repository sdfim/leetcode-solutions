# First Bad Version
# Problem: https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    # Mocking the API for local testing
    # Assuming first bad version is 4 (set manually for test)
    return version >= 4

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
                
        return left

if __name__ == "__main__":
    solution = Solution()
    print(solution.firstBadVersion(5))  # Output: 4 (based on mock)
