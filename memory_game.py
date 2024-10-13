import random
import time

from utils import Screen_cleaner


def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]


def get_list_from_user(difficulty):
    print(f"Enter {difficulty} numbers separated by space:")
    return list(map(int, input().split()))


def is_list_equal(original, user_list):
    return original == user_list


def play(difficulty):
    sequence = generate_sequence(difficulty)
    print("Remember this sequence:")
    print(sequence)
    time.sleep(0.7)  # Display the sequence for 0.7 seconds
    Screen_cleaner()
    user_list = get_list_from_user(difficulty)
    if is_list_equal(sequence, user_list):
        print("Correct sequence!")
        return True
    else:
        print("Wrong sequence!")
        return False
