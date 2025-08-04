class CrosswordBuilder:
    def __init__(self, size=10):
        self.grid = [[" " for _ in range(size)] for _ in range(size)]
        self.size = size

    def word_horizontally(self, word, row, col):
        if col + len(word) > self.size:
            return False
        for i in range(len(word)):
            cell = self.grid[row][col + i]
            if cell != " " and cell != word[i]:
                return False
        return True

    def place_word(self, word, row, col):
        for i in range(len(word)):
            self.grid[row][col + i] = word[i]

    def print_grid(self):
        for row in self.grid:
            print(" ".join(cell if cell != " " else "_" for cell in row))