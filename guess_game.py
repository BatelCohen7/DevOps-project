# Import necessary library
import random


def generate_number(difficulty):
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    return int(input(f"Guess a number between 0 and {difficulty}: "))


def compare_results(secret_number, guess):
    return secret_number == guess


def play(difficulty):
    # Generate a secret number
    secret_number = generate_number(difficulty)
    # Get user's guess
    guess = get_guess_from_user(difficulty)
    # Compare results and return the outcome
    if compare_results(secret_number, guess):
        print("Congratulations! You guessed correctly.")
        return True
    else:
        print(f"Sorry, the correct number was {secret_number}. Better luck next time!")
        return False


#  A driver code to test the game:
if __name__ == "__main__":
    difficulty_level = int(input("Enter the difficulty level (0 to n): "))
    play(difficulty_level)
