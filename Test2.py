x = "101010"
l = len(x)
deci = 0
for n in range (-1, -(l+1), -1):
    deci = deci + (int(x[n]))*(2**(abs(int(n))-1))
print(deci)
