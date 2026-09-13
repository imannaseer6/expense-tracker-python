Project 2 — Number Guessing Game

import random


def get_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    while True:
        choice = input("Enter choice (1-3): ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 50
        elif choice == "3":
            return 100
        else:
            print("Invalid choice.")


def play_game():
    maximum = get_difficulty()
    secret_number = random.randint(1, maximum)
    attempts = 0

    print(f"\nGuess a number between 1 and {maximum}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > maximum:
            print(f"Enter a number between 1 and {maximum}.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Higher!")
        elif guess > secret_number:
            print("Lower!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            return attempts


def main():
    best_attempts = None

    print("===== NUMBER GUESSING GAME =====")

    while True:
        attempts = play_game()

        if best_attempts is None or attempts < best_attempts:
            best_attempts = attempts
            print("New best score:", best_attempts)

        print("Best score:", best_attempts)

        replay = input("\nPlay again? (y/n): ").lower()

        if replay != "y":
            print("Thanks for playing!")
            break


main()
