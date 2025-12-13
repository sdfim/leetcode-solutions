# Split Array into Fibonacci Sequence
# Problem: https://leetcode.com/problems/split-array-into-fibonacci-sequence/
# Solution:

from typing import List

def splitIntoFibonacci(s: str) -> List[int]:
    def backtrack(index, path):
        if index == len(s) and len(path) >= 3:
            return path[:]

        for end in range(index + 1, len(s) + 1):
            num = s[index:end]
            if num[0] == "0" and len(num) > 1:
                break
            num = int(num)
            if num > 2**31 - 1:
                break
            if len(path) < 2 or path[-1] + path[-2] == num:
                path.append(num)
                result = backtrack(end, path)
                if result:
                    return result
                path.pop()

        return []

    return backtrack(0, [])

if __name__ == "__main__":
    s = "123456579"
    print(splitIntoFibonacci(s))
