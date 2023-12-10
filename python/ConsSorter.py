print("Input string pls childs:")
x = input()
y = []

for n in x:
    if n in "aeiou":
        continue
    else:
        y.append(n)

y.sort()
print(y)
