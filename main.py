from Crossword_solver import CrosswordSolver
from builder import CrosswordBuilder

def main():
    words = ["apple", "pear", "banana", "kiwi", "melon"]
    builder = CrosswordBuilder()

    placed_words = []
    for word in sorted(words, key=len, reverse=True):
        placed = builder.try_place_word(word)
        if placed:
            placed_words.append(word)

    builder.fill()
    builder.print_grid()
    solver = CrosswordSolver()
    found = solver.solver(builder.grid, placed_words)
    print("Im Grid gefunden:", found)

    positon = solver.find_word_positions(builder.grid, placed_words)

    for word, coordinates in positon.items():
        print(f"{word}: {coordinates}")

if __name__ == "__main__":
    main()
