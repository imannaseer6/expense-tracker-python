
import random

words = ["PYTHON", "COMPUTER", "HANGMAN", "SCIENCE", "PROGRAM"]

stages = [
    " +---+\n     |\n     |\n     |\n    ===",
    " +---+\n O   |\n     |\n     |\n    ===",
    " +---+\n O   |\n |   |\n     |\n    ===",
    " +---+\n O   |\n/|   |\n     |\n    ===",
    " +---+\n O   |\n/|\\  |\n     |\n    ===",
    " +---+\n O   |\n/|\\  |\n/    |\n    ===",
    " +---+\n O   |\n/|\\  |\n/ \\  |\n    ==="
]

secret_word = random.choice(words)
guessed_letters = set()
wrong_letters = set()
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    print(stages[6 - attempts])

    display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("\nWord:", display)
    print("Guessed letters:", sorted(guessed_letters | wrong_letters))
    print("Attempts left:", attempts)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters or guess in wrong_letters:
        print("You already guessed that letter!")
        continue

    if guess in secret_word:
        guessed_letters.add(guess)
        print("Correct guess!")
    else:
        wrong_letters.add(guess)
        attempts -= 1
        print("Wrong guess!")

else:
    print(stages[6])
    print("Game over! The word was:", secret_word)

print("Thanks for playing!")
