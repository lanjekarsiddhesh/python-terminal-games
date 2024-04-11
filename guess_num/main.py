from art import logo
import random

num = random.randint(1, 100)

print(logo)

print("Welcome to the Number Guessing Game!")

difficulty = input("Select which level are playing Easy/Hard:- ").capitalize()

if difficulty == 'Easy':
    level = 10
else:
    level = 5

level_count = 0
while level_count < level:

    player = int(input("Guess the number between 1 to 100:- "))

    remain = level - level_count - 1
    if player > num:
        print("You guessing the number is high.")
    elif player < num:
        print("You guessing the number is low.")
    else:
        print(f"Your guessing number is correct {num}.")
        print(f"You guess the correct number into {level_count + 1} chances")
        break

    if remain == 0:
        False
    else:
        print(f"Your remaining chancec is {remain}")

    if level_count == level - 1:
        print(f"You lose this game!!! Correct number is {num}")

    level_count += 1









