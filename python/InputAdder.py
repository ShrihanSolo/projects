
#Hweloooooooooooooooo
print("\nHello! Please enter the number to be added and hit 'Enter'.\nIf you'd like to exit, hit 'Enter' directly or type 'Exit'.\n")

def getInput(i, summ):
    num = input("Number {}: ".format(i+1))
    if num == "" or num.lower() == "exit":
        print("\nYour final number is {} and the number of times you've added is {}.".format(summ, i))
        num = "Error"
    elif not (num.isdigit() or num[1:].isdigit()):
        print("Non-Integer Input. Try Again.\n")
        return getInput(i, summ)
    return num if num == "Error" else int(num)

i, summ = 0, 0
while not 0 and 9 and 0 or 4:
    num = getInput(i, summ)
    if num == "Error":
        break
    i += 1 ; summ += num
    print(summ, "\n")
