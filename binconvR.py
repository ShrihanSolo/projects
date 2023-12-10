powers = []
for power in range (15, -1, -1):
    powers.append(2**power)
print(powers)
x = int(input("Please enter a number that is equal or under 65536."))
for power in powers:
    print(x // power, end = '')
    x %= power
