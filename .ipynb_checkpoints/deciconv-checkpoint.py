print("Enter the binary number:")
bin = input()
l = len(bin)
deci = 0
for n in range (-1, -(l+1), -1):
    deci = deci + (int(bin[n]))*(2**(abs(int(n))-1))
print("Converting...")
print(deci)
