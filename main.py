import random
from ascii import Ascii

A = Ascii()

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors:"))
comp = random.randint(0, 2)

if (choice == 0 and comp == 0) or (choice == 1 and comp == 1) or (choice == 2 and comp == 2):
    print("You chose:")
    A.art(selection=choice)
    print("computer chose:")
    A.art(selection=comp)
    print("It is a draw!")
elif (choice == 0 and comp == 1) or (choice == 1 and comp == 2) or (choice == 2 and comp == 0):
    print("You chose:")
    A.art(selection=choice)
    print("Computer chose:")
    A.art(selection=comp)
    print("You lose!")
elif (choice == 0 and comp == 2) or (choice == 1 and comp == 0) or (choice == 2 and comp == 1):
    print("You chose:")
    A.art(selection=choice)
    print("computer chose:")
    A.art(selection=comp)
    print("You win!")
else:
    print("Kindly enter valid input!")
