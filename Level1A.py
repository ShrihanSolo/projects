alphabet = "abcdefghijklmnopqrstuvwxyz"
print("Input code.")
code = input()
print("Translating...")
for i in code:
    if i in alphabet:
        j = alphabet.index(i)
        if (j+2) > 25:
            print(alphabet[j-24], end = '')
        else:
            print(alphabet[j+2], end = '')
    else:
        print(i, end = '')

print(" ")
