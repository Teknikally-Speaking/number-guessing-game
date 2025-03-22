# Number Guessing Game
# Author: [Your Name]
# Date: [Today's Date]

import random

def generate_random_number():
    """Generates and returns a random number between 1 and 100."""
    return random.randint(1, 100)

def get_user_guess():
    """Prompts the user to enter a guess and returns it as an integer."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("❗ Please enter a number between 1 and 100.")
        except ValueError:
            print("❗ Invalid input. Please enter a number.")

def check_guess(secret_number, guess):
    """Compares the user's guess to the secret number and provides feedback."""
    if guess < secret_number:
        print("📉 Too low. Try again!")
    elif guess > secret_number:
        print("📈 Too high. Try again!")
    else:
        print("🎉 Correct! You guessed the number!")

def play_game():
    """Main function to play the number guessing game."""
    print("🎮 Welcome to the Number Guessing Game!")
    secret_number = generate_random_number()
    attempts = 0
    guess = None

    while guess != secret_number:
        guess = get_user_guess()
        attempts += 1
        check_guess(secret_number, guess)

    print(f"👏 It took you {attempts} tries to guess the number.")

# Run the game
if __name__ == "__main__":
    play_game()
