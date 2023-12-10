import random
code = str(random.randint(1000,10000))
i = 0
b = 0

while b != 4:
    c = 0
    b = 0
    print("Enter your guess:")
    guess = input()

    for n in guess:
        for m in code:
            if n == m:
                c += 1

    for n in guess:
        p = guess.index(n)
        for m in code:
            q = code.index(m)
            if p == q and n == m:
                b += 1
    i += 1
    print(str(c)+" cows and "+str(b)+" bulls.")
print("You took "+str(i)+" guess(es).")
