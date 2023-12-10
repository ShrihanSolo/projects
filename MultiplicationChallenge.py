import random
import time


n = int(input("Enter the number you wish to do tables till: "))
print("Press Enter to Begin.")
p = input()

count = 120
cor = 0
wro = 0
i = 0
start = time.time()
while True:
    end = time.time()
    if (end-start) >= 60:
        break
    no1 = random.randint(0,n)
    no2 = random.randint(0,n)
    print("What is "+str(no1)+" x "+str(no2)+"?")
    while True:
        answe = input()
        if answe == "":
            continue
        else:
            break
    answer = int(answe)
    if answer == (no1)*(no2):
        cor += 1
        print("Correct!")
    if answer != (no1)*(no2):
        wro += 1
        print("Incorrect!")

print("Correct: "+str(cor))
print("Wrong: "+str(wro))
print("Time elapsed: "+str(int(end-start))+" seconds")
