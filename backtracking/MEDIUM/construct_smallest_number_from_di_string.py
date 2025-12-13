# Construct Smallest Number From DI String
# Problem: https://leetcode.com/problems/construct-smallest-number-from-di-string/
# Solution:

def smallestNumber(pattern: str) -> str:
    def backtrack(index, stack):
        if index == len(pattern):
            return "".join(stack)
        for num in range(1, 10):
            if str(num) not in stack:
                stack.append(str(num))
                if pattern[index] == "I" and (not stack or stack[-1] < str(num)):
                    result = backtrack(index + 1, stack)
                    if result:
                        return result
                elif pattern[index] == "D" and (not stack or stack[-1] > str(num)):
                    result = backtrack(index + 1, stack)
                    if result:
                        return result
                stack.pop()
        return ""

    return backtrack(0, [])

if __name__ == "__main__":
    pattern = "IDID"
    print(smallestNumber(pattern))
