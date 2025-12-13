# Minimum Unique Word Abbreviation
# Problem: https://leetcode.com/problems/minimum-unique-word-abbreviation/
# Solution:

from typing import List

def minAbbreviation(target: str, dictionary: List[str]) -> str:
    def generate_abbreviations(word):
        n = len(word)
        for i in range(1 << n):
            abbr, count = "", 0
            for j in range(n):
                if i & (1 << j):
                    count += 1
                else:
                    if count:
                        abbr += str(count)
                        count = 0
                    abbr += word[j]
            if count:
                abbr += str(count)
            yield abbr

    valid_abbrs = set(generate_abbreviations(target))
    for word in dictionary:
        valid_abbrs -= set(generate_abbreviations(word))

    return min(valid_abbrs, key=len)

if __name__ == "__main__":
    target = "apple"
    dictionary = ["blade", "plain", "amber"]
    print(minAbbreviation(target, dictionary))
