import random
import getpass

P1W = 0
P2W = 0

def game():
    global P1W
    global P2W

    print(P1name+", please enter your guess (A number between 1 and 100):")
    P1 = int(getpass.getpass())
    print(P2name+", please enter your guess (A number between 1 and 100):")
    P2 = int(getpass.getpass())

    Comp = random.randint(1,100)

    P1Diff = abs(P1 - Comp)
    P2Diff = abs(P2 - Comp)

    if P1Diff < P2Diff:
        print(P1name+"'s number was "+str(P1)+" and "+P2name+"'s number was "+str(P2)+".")
        print(P1name+" wins! The number is "+str(Comp)+"!")
        P1W = P1W + 1
        print("The score is "+str(P1W)+"-"+str(P2W))
    elif P1Diff > P2Diff:
        print(P1name+"'s number was "+str(P1)+" and "+P2name+"'s number was "+str(P2)+".")
        print(P2name+" wins! The number is "+str(Comp)+"!")
        P2W = P2W + 1
        print("The score is "+str(P1W)+"-"+str(P2W))
    else:
        print(P1name+"'s number was "+str(P1)+" and "+P2name+"'s number was "+str(P2)+".")
        print("It's a tie! The number was "+str(Comp)+"!")
        print("Its time to restart the game!")
        print("The score is "+str(P1W)+"-"+str(P2W))
        game()

i = 0
print("How many times do you want to play?")
play = int(input())
print("What is Player 1's name?")
P1name = input()
print("What is Player 2's name?")
P2name = input()

while i < play:
    game()
    i += 1
else:
    print("Thank you for playing!")
