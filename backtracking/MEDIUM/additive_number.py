# Additive Number
# Problem: https://leetcode.com/problems/additive-number/
# Solution:

def isAdditiveNumber(num: str) -> bool:
    def backtrack(start, path):
        if start == len(num) and len(path) >= 3:
            return True

        for end in range(start + 1, len(num) + 1):
            if num[start] == "0" and end > start + 1:
                break

            curr = int(num[start:end])
            if len(path) < 2 or path[-1] + path[-2] == curr:
                path.append(curr)
                if backtrack(end, path):
                    return True
                path.pop()

        return False

    return backtrack(0, [])

if __name__ == "__main__":
    num = "112358"
    print(isAdditiveNumber(num))
