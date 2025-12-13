# Expression Add Operators
# Problem: https://leetcode.com/problems/expression-add-operators/
# Solution:

from typing import List

def addOperators(num: str, target: int) -> List[str]:
    def backtrack(index, prev_operand, current_operand, value, expression):
        if index == len(num):
            if value == target and current_operand == 0:
                results.append("".join(expression[1:]))
            return

        current_operand = current_operand * 10 + int(num[index])
        str_operand = str(current_operand)

        if current_operand > 0:
            backtrack(index + 1, prev_operand, current_operand, value, expression)

        expression.append("+")
        expression.append(str_operand)
        backtrack(index + 1, current_operand, 0, value + current_operand, expression)
        expression.pop()
        expression.pop()

        if expression:
            expression.append("-")
            expression.append(str_operand)
            backtrack(index + 1, -current_operand, 0, value - current_operand, expression)
            expression.pop()
            expression.pop()

            expression.append("*")
            expression.append(str_operand)
            backtrack(index + 1, prev_operand * current_operand, 0, value - prev_operand + (prev_operand * current_operand), expression)
            expression.pop()
            expression.pop()

    results = []
    backtrack(0, 0, 0, 0, [])
    return results

if __name__ == "__main__":
    num = "123"
    target = 6
    print(addOperators(num, target))
