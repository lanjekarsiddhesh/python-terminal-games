import random
from ascii_art import logo, stages
from words import lst
from result import win, loss

print(logo)

chs = random.choice(lst)

lent = len(chs)

chs_lst = []
print(f"Your words in total {lent} alphabate")

First_char = chs[0]
second_char = chs[lent - 1]

for _ in range(lent):
    chs_lst += '_'


lives = 6

while True:
    chs_lst[0] = First_char
    chs_lst[lent-1] = second_char
    print(f"Complete the following word \n {chs_lst}")
    
    user = input("Choose a letter to releted word:- ").lower()

    if user in chs_lst:
        print(f"You've already guessed {user}")

    for position in range(lent):
        letter = chs[position]
        if letter == user:
            chs_lst[position] = letter

    if "_" not in chs_lst:
        lives -= 1
        if lives == 0:
            print(chs_lst)
        print(" ")
        print(win)
        # print("You win.")
        print(f"Your word is :- {''.join(chs_lst)}")
        break

    if user not in chs:
        lives -= 1
        print(stages[lives])
        print(f"you choose wrong letter, your remaining life is:- {lives}")
        print(" ")

        if lives == 0:
            print(loss)
            print(f"Your word is :- {chs}")
            break

    print(chs_lst)



