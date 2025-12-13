# Numbers With Same Consecutive Differences
# Problem: https://leetcode.com/problems/numbers-with-same-consecutive-differences/
# Solution:

from typing import List

def numsSameConsecDiff(n: int, k: int) -> List[int]:
    def backtrack(num, length):
        if length == n:
            result.append(num)
            return

        last_digit = num % 10
        next_digits = {last_digit + k, last_digit - k}
        for next_digit in next_digits:
            if 0 <= next_digit <= 9:
                backtrack(num * 10 + next_digit, length + 1)

    result = []
    for i in range(1, 10):
        backtrack(i, 1)
    return result

if __name__ == "__main__":
    n, k = 3, 7
    print(numsSameConsecDiff(n, k))
