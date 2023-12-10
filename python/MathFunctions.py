import math

def f(x):
    return math.cos(x)

i = 0
print("Number of iterations?")
n = input()
print("Starting Value?")
x = 6

while (i < n):
    i += 1
    def f(x):
        return math.cos((f(x)))
    print(f(x))

else:
    print("Done!")
