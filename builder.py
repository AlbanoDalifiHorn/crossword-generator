import random
import string

from unicodedata import east_asian_width


class CrosswordBuilder:
    def __init__(self, size=10, allowed_directions=None):
        self.grid = [[" " for _ in range(size)] for _ in range(size)]
        self.size = size
        self.allowed_directions = allowed_directions or ["horizontal", "vertical", "diagonal_right_down", "diagonal_right_up"]


    def word_horizontal(self, word, row, col):
        if col + len(word) > self.size:
            return False
        for i in range(len(word)):
            cell = self.grid[row][col + i]
            if cell != " " and cell != word[i]:
                return False
        return True

    def word_vertical(self, word, row, col):
        if row + len(word) > self.size:
            return False
        for i in range(len(word)):
            cell = self.grid[row + i][col]
            if cell != " " and cell != word[i]:
                return False
        return True

    def word_diagonal_right_down(self, word, row, col):
        if row + len(word) > self.size or col + len(word) > self.size:
            return False
        for i in range(len(word)):
            cell = self.grid[row + i][col + i]
            if cell != " " and cell != word[i]:
                return False
        return True

    def word_diagonal_right_up(self, word, row, col):
        if row - len(word) + 1 < 0 or col + len(word) > self.size:
            return False
        for i in range(len(word)):
            cell = self.grid[row - i][col + i]
            if cell != " " and cell != word[i]:
                return False
        return True

    def word_diagonal_left_down(self, word, row, col):
        if row + len(word) > self.size or col - len(word) + 1 < 0:
            return False
        for i in range(len(word)):
            cell= self.grid[row + i][col - i]
            if cell != " " and cell != word[i]:
                return False
        return True

    def word_diagonal_left_up(self, word, row, col):
        if row - len(word) + 1 < 0 or col - len(word) + 1 < 0:
            return False
        for i in range(len(word)):
            cell = self.grid[row - i][col - i]
            if cell != " " and cell != word[i]:
                return False
        return True

    def place_horizontal(self, word, row, col):
        for i in range(len(word)):
            self.grid[row][col + i] = word[i]

    def place_vertical(self, word, row, col):
        for i in range(len(word)):
            self.grid[row + i][col] = word[i]

    def place_diagonal_right_up(self, word, row, col):
        for i in range(len(word)):
            self.grid[row - i][col + i] = word[i]

    def place_diagonal_right_down(self, word, row, col):
        for i in range(len(word)):
            self.grid[row + i][col + i] = word[i]

    def place_diagonal_left_up(self, word, row, col):
        for i in range(len(word)):
            self.grid[row - i][col + i] = word[i]

    def place_diagonal_left_down(self, word, row, col):
        for i in range(len(word)):
            self.grid[row + i][col - i] = word[i]

    def try_place_word(self, word, max_attempts=100, placed_words=None):
        if placed_words and word in placed_words:
            return False

        directions = ["horizontal", "vertical", "diagonal_right_down", "diagonal_right_up", "diagonal_left_down", "diagonal_left_up"]
        for i in range(max_attempts):
            dir = random.choice(directions)
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            if dir == "horizontal" and self.word_horizontal(word, row, col):
                self.place_horizontal(word, row, col)
                return True
            elif dir == "vertical" and self.word_vertical(word, row, col):
                self.place_vertical(word, row, col)
                return True
            elif dir == "diagonal_right_up" and self.word_diagonal_right_up(word, row, col):
                self.place_diagonal_right_up(word, row, col)
                return True
            elif dir == "diagonal_right_down" and self.word_diagonal_right_down(word, row, col):
                self.place_diagonal_right_down(word, row, col)
                return True
            elif dir == "diagonal_left_up" and self.word_diagonal_left_up(word, row, col):
                self.place_diagonal_left_up(word, row, col)
            elif dir == "diagonal_left_down" and self.word_diagonal_left_down(word, row, col):
                self.place_diagonal_left_down(word, row, col)
            if dir not in directions:
                continue
        return False

    def fill(self):
        for row in range(self.size):
            for cell in range(self.size):
                if self.grid[row][cell] == " ":
                    self.grid[row][cell] = random.choice(string.ascii_lowercase)

    def print_grid(self):
        for row in self.grid:
            print(" ".join(cell if cell != " " else "_" for cell in row))