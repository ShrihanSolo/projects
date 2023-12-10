x = 0
y = 1
i = 0

n = input("Input number in sequence:")

print(str(x))
print(str(y))

while i < (int(n)-2):
    z = x+y
    x = y
    y = z
    print(z)
    i += 1
