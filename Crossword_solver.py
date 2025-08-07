from typing import List, Dict, Tuple
from trie import Trie

class CrosswordSolver:
    def solver(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        result = set()

        def dfs(node, row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] not in node.children or board[row][col] == '#':
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

    def find_word_positions(self, grid: List[List[str]], words: List[str]) -> Dict[str, List[Tuple[int, int]]]:
        rows, cols = len(grid), len(grid[0])
        positions = {}

        for word in words:
            found = False
            # Suche horizontal
            for r in range(rows):
                for c in range(cols - len(word) + 1):
                    if all(grid[r][c + i] == word[i] for i in range(len(word))):
                        positions[word] = [(r, c + i) for i in range(len(word))]
                        found = True
                        break
                if found: break

            # Suche vertikal
            if not found:
                for c in range(cols):
                    for r in range(rows - len(word) + 1):
                        if all(grid[r + i][c] == word[i] for i in range(len(word))):
                            positions[word] = [(r + i, c) for i in range(len(word))]
                            found = True
                            break
                    if found: break

            if not found:
                # Diagonale: links oben nach rechts unten
                for r in range(rows - len(word) + 1):
                    for c in range(cols - len(word) + 1):
                        if all(grid[r + i][c + i] == word[i] for i in range(len(word))):
                            positions[word] = [(r + i, c + i) for i in range(len(word))]
                            found = True
                            break
                    if found: break

            if not found:
                # Diagonale: links unten nach rechts oben
                for r in range(len(word) - 1, rows):
                    for c in range(cols - len(word) + 1):
                        if all(grid[r - i][c + i] == word[i] for i in range(len(word))):
                            positions[word] = [(r - i, c + i) for i in range(len(word))]
                            found = True
                            break
                    if found: break
        return positions