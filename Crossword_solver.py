from typing import List
from trie import Trie


class CrosswordSolver:
    def solver(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        result = set()

        def dfs(node, row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] not in node.children:
                return

            char = board[row][col]
            node = node.children[char]

            if node.is_word:
                result.add(node.word)
                node.is_word = False

            board[row][col] = '#'

            dfs(node, row, col + 1)
            dfs(node, row + 1, col)
            dfs(node, row - 1, col)
            dfs(node, row, col - 1)

            board[row][col] = char

        for r in range(rows):
            for c in range(cols):
                dfs(trie.root, r, c)

        return list(result)
