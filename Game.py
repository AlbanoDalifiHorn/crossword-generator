from builder import CrosswordBuilder
from Crossword_solver import CrosswordSolver

class CrosswordGame:
    def __init__(self, size=10):
        self.size = size
        self.builder = None
        self.solver = CrosswordSolver()
        self.word_placed = []
        self.found = set()
        self.max_word_length = 8
        self.allowed_directions = ["horizontal", "vertical", "diagonal_right_down", "diagonal_right_up"]
        self.result = []

    def set_mode(self, mode: str):
        mode = mode.lower()
        if mode == "easy":
            self.max_word_length = 5
            self.allowed_directions = ["horizontal", "vertical"]
        elif mode == "medium":
            self.max_word_length = 7
            self.allowed_directions = ["horizontal", "vertical", "diagonal_right_down"]
        elif mode == "hard":
            self.max_word_length = 10
            self.allowed_directions = ["horizontal", "vertical", "diagonal_right_down", "diagonal_right_up"]
        else:
            raise ValueError("Unknown mode")

        self.builder = CrosswordBuilder(size=self.size, allowed_directions=self.allowed_directions)

    def setup(self, words):
        filtered_words = [w.lower() for w in words if len(w) <= self.max_word_length]
        for word in sorted(filtered_words, key=len, reverse=True):
            placed = self.builder.try_place_word(word, max_attempts=100)
            if placed and word not in self.word_placed:
                self.word_placed.append(word)

        if not self.word_placed:
            raise Exception("No words were placed")

        self.builder.fill()
        return len(self.word_placed)

    def display_game_state(self):
        self.builder.print_grid()
        print(f"\nCurrently found: {len(self.found)} / {len(self.word_placed)}")
        if self.found:
            print(f"Found words: {', '.join(sorted(self.found))}")

    def check_word(self, guess):
        guess = guess.strip().lower()
        if guess in self.word_placed:
            if guess in self.found:
                return "already found"
            self.found.add(guess)
            return "correct"
        return "not found"

    def get_word(self, word):
        positions = self.solver.find_word_positions(self.builder.grid, [word])
        return positions.get(word, [])

    def completed(self):
        return len(self.found) == len(self.word_placed)

    def remaining_words(self):
        return set(self.word_placed) - self.found

    def play(self):
        print("\n" + "=" * 50)
        print("Crossword - Game")
        print("=" * 50)
        print("Find all hidden words!")
        print("Input 'quit' to end game\n")

        while not self.completed():
            self.display_game_state()
            guess = input("\nGuess a word: ")
            if guess.strip().lower() == 'quit':
                break
            result = self.check_word(guess)
            if result == "correct":
                word = guess.strip().lower()
                positions = self.get_word(word)
                self.result.append((word, positions))
                print(f"Correct! '{word}' is at {positions}")
            elif result == "already found":
                print(f"{guess.strip()} was already found")
            else:
                print(f"{guess.strip()} is not in the crossword")

        if self.completed():
            print("Congratulations! You found every word","\n", self.result)
        else:
            print(f"\nGame Over 😔. Remaining words: {', '.join(self.remaining_words())}")
