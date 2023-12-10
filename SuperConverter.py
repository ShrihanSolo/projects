print("For binary to decimal, enter 'bin'. For decimal to binary, enter 'deci':")
k = input()

if k == "bin":
    j = 64
    print("Enter the decimal number [Below 2^"+str(j)+" ("+str(2**j)+")]:")
    deci = int(input()) + 1
    bin = ""
    while j >= 0:
        if deci > (2**j):
            i = str(1)
            deci = deci - (2**j)
        else:
            i = str(0)
        bin = bin + i
        j = j - 1
    print("Converting to binary...")
    print(str(int(bin)))
elif k == "deci":
    print("Enter the binary number:")
    bin = input()
    l = len(bin)
    deci = 0
    for n in range (-1, -(l+1), -1):
        deci = deci + (int(bin[n]))*(2**(abs(int(n))-1))
    print("Converting to decimal...")
    print(deci)
else:
    print("You have not entered a valid input. Please enter only 'bin' or 'deci'.")
