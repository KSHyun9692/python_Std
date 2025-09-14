""" from random import randint

user_choice = int(input("choose number"))
pc_choice = 50
pc_choice2 = randint(1, 50)

if user_choice == pc_choice:
    print("you won")
elif user_choice > pc_choice:
    print("lower")
elif user_choice < pc_choice:
    print("higher")


if user_choice == pc_choice2:
    print("you won")
elif user_choice > pc_choice2:
    print("lower computer chose", pc_choice2)
elif user_choice < pc_choice2:
    print("higher computer chose", pc_choice2)
 """
"""
주석

"""
#주석


""" distance = 0

while(distance < 20):
    print("i'm running: ", distance, "km")
    distance = distance + 1 """

from random import randint

playing = True
pc_choice = randint(1, 50)

while playing:
    user_choice = int(input("choose number"))
    if user_choice == pc_choice:
        print("you won")
        playing = False
    elif user_choice > pc_choice:
        print("lower")
    elif user_choice < pc_choice:
        print("higher")