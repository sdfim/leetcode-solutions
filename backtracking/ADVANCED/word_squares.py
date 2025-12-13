# Word Squares
# Problem: https://leetcode.com/problems/word-squares/
# Solution:

from typing import List

def wordSquares(words: List[str]) -> List[List[str]]:
    def build_trie():
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["$"] = word
        return trie

    def backtrack(step):
        if step == n:
            results.append(list(square))
            return

        prefix = "".join(square[i][step] for i in range(step))
        node = trie
        for char in prefix:
            if char not in node:
                return
            node = node[char]

        for char in node:
            if char != "$":
                square.append(node[char])
                backtrack(step + 1)
                square.pop()

    n = len(words[0])
    trie = build_trie()
    results, square = [], []
    for word in words:
        square.append(word)
        backtrack(1)
        square.pop()
    return results

if __name__ == "__main__":
    words = ["area", "lead", "wall", "lady", "ball"]
    print(wordSquares(words))
