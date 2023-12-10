import random
code = list(str(random.randint(1000,10000)))
i = 0
b = 0

def guessfn():
    global guess
    print("Enter your guess:")
    guess = list(str(input()))
    for m in guess:
        if m not in "1234567890" or len(guess) != 4:
            print("Incorrect input, try again.")
            guessfn()
            break

while b != 4:
    c = 0
    b = 0
    j = 0
    k = 0
    n = 0
    l = []
    guess = []
    print("Attempt Number "+str(i+1))
    guessfn()
    while j < 4:
        if guess[j] == code[j]:
            b += 1
            l.append(str(j))
        j += 1
    while k < 4:
        if guess[k] == code[k]:
            k += 1
            continue
        for n in range(0,4):
            if str(n) in l:
                continue
            elif guess[k] == code[n]:
                c += 1
        k += 1
    i += 1
    print(str(c)+" cow(s) and "+str(b)+" bull(s).")
if b == 4:
    print("You took "+str(i)+" guess(es).")
print("Thank you for playing!")
