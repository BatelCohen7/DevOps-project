import CurrencyRouletteGame
import GuessGame
import MemoryGame

def start_play():
    print("""
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS.
    """)

    while True:
        try:
            game_choice = int(input("Enter the number of the game you want to play: "))
            if game_choice in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            difficulty = int(input("Now enter the difficulty level between 1 and 5: "))
            if 1 <= difficulty <= 5:
                print(f"You have selected difficulty level {difficulty}.")
                break
            else:
                print("Invalid input. Please enter a difficulty level between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("We are about to start the game, prepare ;)")

    if game_choice == 1:
        MemoryGame.play(difficulty)
    elif game_choice == 2:
        GuessGame.play(difficulty)
    elif game_choice == 3:
        CurrencyRouletteGame.play(difficulty)
