from Game import CrosswordGame

def main():
    words = ["apple", "banana", "kiwi", "melon", "cherry", "frankreich"]

    try:
        game = CrosswordGame(size=10)

        mode = input("Choose difficulty (easy, medium, hard): ")

        game.set_mode(mode)
        game.setup(words)
        game.play()

    except Exception as e: print(f" failed by start: {e}")

if __name__ == "__main__":
    main()