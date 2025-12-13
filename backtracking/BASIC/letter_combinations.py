# Letter Combinations of a Phone Number
# Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Solution:

from typing import List

def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    def backtrack(index, path):
        if index == len(digits):
            combinations.append("".join(path))
            return

        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations

if __name__ == "__main__":
    digits = "23"
    print(letterCombinations(digits))
