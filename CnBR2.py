randomNumber = "7308"
randomNumberList = []
letters = "abcdefghijklmnaopqrstuvwxyzABCDEFGHIJKLMNAOPQRSTUVWXYZ"
for number in randomNumber:
    randomNumberList.append(number)

print(randomNumberList)

cow = 0
bull = 0

while True:
    guess = input("Please enter a 4-digit number: ")
    guessList = []
    for char in guess:
        guessList.append(char)
    print(guessList)

    if randomNumberList[0] == guessList [0]:
        cow += 1
    if randomNumberList[1] == guessList[1]:
        cow += 1
    if randomNumberList[2] == guessList[2]:
        cow += 1
    if randomNumberList[3] == guessList[3]:
        cow += 1
    print(str(cow) + " cows")

    for char in guessList:
        if char in randomNumberList:
            bull += 1

    print(str(bull) + " bulls")
