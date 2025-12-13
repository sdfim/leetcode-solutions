from typing import List

# Solution:
# Problem: https://leetcode.com/problems/generalized-abbreviation/


def generateAbbreviations(word: str) -> List[str]:
    def backtrack(index, count, path):
        if index == len(word):
            result.append("".join(path) + (str(count) if count > 0 else ""))
            return
        # Abbreviate the current index
        backtrack(index + 1, count + 1, path)
        # Stop abbreviation and add the current word[index]
        path.append(word[index])
        if count > 0:
            # If count is greater than 0, we have abbreviated some characters
            # Add the count to the abbreviation
            path.append(str(count))
        # Move to the next index
        backtrack(index + 1, 0, path)
        # Backtrack: remove the current word[index] and count
        path.pop()
        if count > 0:
            path.pop()

    result = []
    backtrack(0, 0, [])
    return result


if __name__ == "__main__":
    word = "word"
    print(generateAbbreviations(word))
