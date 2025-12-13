# Maximum Score Words Formed by Letters
# Problem: https://leetcode.com/problems/maximum-score-words-formed-by-letters/
# Solution:

from typing import List
from collections import Counter

def maxScoreWords(words: List[str], letters: List[str], score: List[int]) -> int:
    def backtrack(index, current_score):
        if index == len(words):
            return current_score

        max_score = backtrack(index + 1, current_score)
        word_count = Counter(words[index])
        if all(word_count[char] <= letter_count[char] for char in word_count):
            for char in word_count:
                letter_count[char] -= word_count[char]
            max_score = max(max_score, backtrack(index + 1, current_score + sum(score[ord(char) - ord('a')] * word_count[char] for char in word_count)))
            for char in word_count:
                letter_count[char] += word_count[char]

        return max_score

    letter_count = Counter(letters)
    return backtrack(0, 0)

if __name__ == "__main__":
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "g", "o", "o"]
    score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(maxScoreWords(words, letters, score))
