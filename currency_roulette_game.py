import requests


def get_money_interval(difficulty, amount_usd=100):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    rate = response.json()['rates']['ILS']
    converted_amount = amount_usd * rate
    margin = 10 - difficulty
    return (converted_amount - margin, converted_amount + margin)


def get_guess_from_user():
    return float(input("Enter your guess for the amount in ILS: "))


def compare_results(interval, guess):
    return interval[0] <= guess <= interval[1]


def play(difficulty):
    interval = get_money_interval(difficulty)
    guess = get_guess_from_user()
    if compare_results(interval, guess):
        print("Correct! Well done.")
        return True
    else:
        print("Incorrect guess. Try again.")
        return False
