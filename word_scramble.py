import random
import os

# Fallback built-in word list (if words.txt is missing)
DEFAULT_WORDS = [
    "proteasome", "ubiquitin", "ribosome", "chromatin", "nucleotide",
    "polymerase", "transcription", "translation", "mitochondria",
    "phosphorylation", "signal", "cytoskeleton", "kinase",
    "chaperone", "replication", "helicase", "exon", "intron",
    "epigenetics", "autophagy"
]


def load_words():
    """
    Load words from words.txt.
    If the file doesn't exist, use DEFAULT_WORDS.
    """
    try:
        with open("words.txt", "r") as f:
            words = [line.strip() for line in f if line.strip()]
            if words:
                return words
        # Empty file → fallback
        return DEFAULT_WORDS
    except FileNotFoundError:
        return DEFAULT_WORDS


def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


def get_highscore():
    """Reads the saved high score from highscore.txt"""
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read().strip())
    except:
        return 0


def save_highscore(score):
    """Saves a new high score if the player achieved one"""
    high = get_highscore()
    if score > high:
        with open("highscore.txt", "w") as f:
            f.write(str(score))
        print("🏆 New high score!\n")


def play_game():
    print("\n🔬 Welcome to the Science Word Scramble Game! 🔬")
    print("Unscramble the science word. Type 'quit' to exit.\n")

    words = load_words()
    score = 0

    while True:
        word = random.choice(words)
        scrambled = scramble_word(word)

        print(f"Scrambled word: {scrambled}")
        guess = input("Your guess: ").strip().lower()

        if guess == "quit":
            print(f"\nGame over! Your final score is: {score}")
            save_highscore(score)
            print(f"Highest score so far: {get_highscore()}")
            break

        if guess == word:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Nope! The correct word was: {word}")
        
        print(f"Current score: {score}\n")


if __name__ == "__main__":
    play_game()
