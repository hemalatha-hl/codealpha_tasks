import random

# Predefined list of words
words = ["apple", "tiger", "chair", "robot", "house"]

# Select a random word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game")

while attempts > 0:
    display_word = ""

    # Show guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess not in word:
        attempts -= 1
        print("Wrong guess")

    # Check win condition
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

else:
    print("\nGame Over! The word was:", word)