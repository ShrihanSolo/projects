def dumb(name, i):
    print(name + " is dumb", end = "")
    for n in range(0, i):
        print("er", end = "")
    if i < (no - 1):
        print("")
i = 0
inpt = input("What's your name?: ")
no = int(input("Pick a number between 1 and...100?: "))
while i < no:
    dumb(inpt, i)
    i += 1
print("EST")
print("Successfully printed " + inpt + " is dumb " + str(no) + " times.")
