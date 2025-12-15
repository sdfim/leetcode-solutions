# Guess Number Higher or Lower
# Problem: https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

PICK = 6

def guess(num: int) -> int:
    if num > PICK:
        return -1
    elif num < PICK:
        return 1
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1
            else:
                right = mid - 1
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.guessNumber(10))  # Output: 6
