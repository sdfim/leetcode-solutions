# Remove Invalid Parentheses
# Problem: https://leetcode.com/problems/remove-invalid-parentheses/
# Solution:

from typing import List

def removeInvalidParentheses(s: str) -> List[str]:
    def is_valid(string):
        count = 0
        for char in string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    level = {s}
    while True:
        valid = list(filter(is_valid, level))
        if valid:
            return valid
        next_level = set()
        for item in level:
            for i in range(len(item)):
                next_level.add(item[:i] + item[i + 1:])
        level = next_level

if __name__ == "__main__":
    s = "()())()"
    print(removeInvalidParentheses(s))
