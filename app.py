def welcome():
    user_name = input("Hi, what is your name? ")
    print(f"Hi {user_name} and welcome to the World of Games: The Epic Journey")

def start_play():
    print("Ple choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS.")

    while True:
        game_choice = input("Enter the number of the game you want to play: ")
        if game_choice in ['1', '2', '3']:
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

    while True:
        difficulty = input("Now enter the difficulty level between 1 and 5: ")
        if difficulty.isdigit() and 1 <= int(difficulty) <= 5:
            print(f"You have selected difficulty level {difficulty}.")
            break
        else:
            print("Invalid input. Please enter a difficulty level between 1 and 5.")

    print("We are about to start the game, prepare ;)")
