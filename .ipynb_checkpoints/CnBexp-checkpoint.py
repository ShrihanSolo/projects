import random

def makeCode():
    """Makes a computer generated code."""

    code, i = [], 0
    while i < 4:
        code.append(random.randint(0, 9))
        i += 1
    return code

def checkCows(code, guess):
    """Checks number of Cows for a guess.

    >>> checkCows([1,2,3,4], [4,3,2,1])
    4
    >>> checkCows([1,3,1,3], [3,1,3,1])
    4
    >>> checkCows([1,2,3,4], [1,3,2,4])
    4
    >>> checkCows([0,1,3,4], [2,1,4,5])
    2
    >>> checkCows([2,1,1,7], [1,5,6,7])
    2
    >>> checkCows([2,1,2,3], [1,1,2,3])
    3
    >>> checkCows([1,1,3,3], [3,3,2,3])
    2
    >>> checkCows([1,1,1,1], [2,3,4,5])
    0
    """

    cow = 0
    checklist = []
    for i in guess:
        check = (i not in checklist)
        num_in_code = code.count(i)
        num_in_guess = guess.count(i)
        if (num_in_code == num_in_guess) and check:
            cow = cow + num_in_code
            checklist.append(i)
        elif (num_in_code > num_in_guess) and check:
            cow = cow + num_in_guess
            checklist.append(i)
        elif (num_in_code < num_in_guess) and check:
            cow = cow + num_in_code
            checklist.append(i)
    return cow

def checkBulls(code, guess):
    """Checks number of bulls for a guess.

    >>> checkBulls([1,3,5,6], [1,3,4,6])
    3
    >>> checkBulls([1,2,3,4], [4,3,2,1])
    0
    >>> checkBulls([1,3,4,5], [1,9,7,5])
    2
    >>> checkBulls([1,2,2,3], [1,2,2,2])
    3
    """
    bull = 0
    for i in range(0, 4):
        if code[i] == guess[i]:
            bull += 1
    return bull

def askGuess():
    def checkInput():
        guess = input("Please Enter Your Guess: ")
        if guess == "":
            print("Input a 4-digit number.")
            return checkInput()
        for num in guess:
            if num not in "1234567890" or len(guess) != 4:
                print("Input a 4-digit number.")
                return checkInput()
                break
        return guess

    guess = int(checkInput())
    guesslist = []
    while guess > 0:
        guess, last = guess // 10, guess % 10
        guesslist.insert(0, last)
    return guesslist



def runGame():
    code, turn, running = makeCode(), 1, True
    while running == True:
        print("Turn", str(turn) +":")
        guess = askGuess()
        bulls = checkBulls(code, guess)
        cows = checkCows(code, guess) - bulls
        print("Your Guess Produced", cows, "Cow(s) and" , bulls, "Bull(s)!")
        turn += 1
        if code == guess:
            running = False
    print("Well Played! You won in", (turn-1), "turn(s)!")
    print("Play Again? (Y/N)")
    again = input()
    if again.upper() == "Y":
        print("Here we go!")
        runGame()
    elif again.upper() == "N":
        print("Thanks for Playing!")

runGame()
