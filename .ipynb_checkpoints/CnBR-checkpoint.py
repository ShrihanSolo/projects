randomNumber = "3333"
randomNumberList = []
letters = "abcdefghijklmnaopqrstuvwxyzABCDEFGHIJKLMNAOPQRSTUVWXYZ"
for number in randomNumber:
    randomNumberList.append(number)


guessNumber = 0

while True:
    playerGuessList = []
    playerGuess = input("Please enter a 4-digit number: ")

    for char in playerGuess:
        playerGuessList.append(char)

    cows = 0
    bulls = 0
    nothing = 0
    for num in playerGuessList:
        if num in randomNumberList:
            cows += 1
        elif num in letters:
            nothing += 1
        else:
            bulls += 1
    if cows + bulls != 4:
        print("That is an invalid entry.")
        continue

    guessNumber += 1

    print(str(cows) + " cows")
    print(str(bulls) + " bulls")
    print("Number of guesses: " + str(guessNumber))


    if cows == 4:
        print("Congrats you have guessed the number.")
        break
