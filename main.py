from builder import CrosswordBuilder

def main():
    words = ["apple", "pear", "banana"]
    builder = CrosswordBuilder()

    if builder.word_horizontally("apple", 0, 0):
        builder.place_word("apple", 0, 0)

    if builder.word_horizontally("pear", 1, 2):
        builder.place_word("pear", 1, 2)

    builder.print_grid()

if __name__ == "__main__":
    main()
