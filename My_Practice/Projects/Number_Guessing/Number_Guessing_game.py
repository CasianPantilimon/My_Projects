"""
guess a number between 1-5
- track the numbers how many times the user tried
"""

import random

number = random.choice(range(1, 50))
# print(number)
tries = 0

while True:
    tries += 1
    try:
        guess = int(input("Guess a number betweeen 1-50: "))
    except ValueError:
        print(f"You must enter numbers, not letters.")
        continue
    if guess not in range(1, 50):
        print("The number must be between: 1-5")
        continue
    if guess in range(1, 50):
        if guess == number:
            print(f"You nailed it. Indeed the number was: {number}")
            print(f"You have tried: {tries} times")
            break
        elif guess != number:
            if guess > number:
                print("You were above the number!")
                continue
            else:
                print("You were bellow the number!")
                continue
