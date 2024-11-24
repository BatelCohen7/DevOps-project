import currency_roulette_game
import guess_game
import memory_game


def start_play():
    print("""
Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS.
""")


    while True:
       game_choice = int(input("Enter the number of the game you want to play: "))
         if game_choice in ['1', '2', '3']:
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

    while True:
        difficulty = input("Now enter the difficulty level between 1 and 5: ")
        if difficulty.isdigit() and 1 <= int(difficulty) <= 5:
            difficulty = int(difficulty)
            print(f"You have selected difficulty level {difficulty}.")
            break
        else:
            print("Invalid input. Please enter a difficulty level between 1 and 5.")

    print("We are about to start the game, prepare ;)")

    if game_choice == '1':
        memory_game.play(difficulty)
    elif game_choice == '2':
        guess_game.play(difficulty)
    elif game_choice == '3':
        currency_roulette_game.play(difficulty)
