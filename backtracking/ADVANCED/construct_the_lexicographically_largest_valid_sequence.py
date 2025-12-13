# Construct the Lexicographically Largest Valid Sequence
# Problem: https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/
# Solution:

from typing import List

def constructDistancedSequence(n: int) -> List[int]:
    def backtrack(index):
        if index == len(sequence):
            return True
        if sequence[index] != 0:
            return backtrack(index + 1)

        for num in range(n, 0, -1):
            if used[num]:
                continue
            if num == 1 or (index + num < len(sequence) and sequence[index + num] == 0):
                sequence[index] = num
                if num != 1:
                    sequence[index + num] = num
                used[num] = True

                if backtrack(index + 1):
                    return True

                sequence[index] = 0
                if num != 1:
                    sequence[index + num] = 0
                used[num] = False

        return False

    sequence = [0] * (2 * n - 1)
    used = [False] * (n + 1)
    backtrack(0)
    return sequence

if __name__ == "__main__":
    n = 3
    print(constructDistancedSequence(n))
