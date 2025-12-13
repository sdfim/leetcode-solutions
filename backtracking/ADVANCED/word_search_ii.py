# Word Search II
# Problem: https://leetcode.com/problems/word-search-ii/
# Solution:

from typing import List

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    def backtrack(node, r, c, path):
        char = board[r][c]
        curr_node = node[char]
        word_match = curr_node.pop("$", False)
        if word_match:
            matched_words.add(word_match)

        board[r][c] = "#"
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] in curr_node:
                backtrack(curr_node, nr, nc, path + board[nr][nc])
        board[r][c] = char

    trie = {}
    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["$"] = word

    matched_words = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in trie:
                backtrack(trie, r, c, "")

    return list(matched_words)

if __name__ == "__main__":
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(findWords(board, words))
