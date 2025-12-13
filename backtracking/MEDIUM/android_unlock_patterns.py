# Android Unlock Patterns
# Problem: https://leetcode.com/problems/android-unlock-patterns/
# Solution:

def numberOfPatterns(m: int, n: int) -> int:
    def is_valid(used, last, next):
        if used[next]:
            return False
        if last == -1:
            return True
        if (last + next) % 2 == 1:
            return True
        mid = (last + next) // 2
        if mid in {4, 5}:
            return used[mid]
        if (last % 3 != next % 3) and (last // 3 != next // 3):
            return True
        return used[mid]

    def backtrack(used, last, length):
        if length == 0:
            return 1
        count = 0
        for next in range(9):
            if is_valid(used, last, next):
                used[next] = True
                count += backtrack(used, next, length - 1)
                used[next] = False
        return count

    used = [False] * 9
    return sum(backtrack(used, -1, length) for length in range(m, n + 1))

if __name__ == "__main__":
    m, n = 1, 2
    print(numberOfPatterns(m, n))
