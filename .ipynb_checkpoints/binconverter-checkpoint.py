#Decimal to binary converter
print("Enter the decimal number:")
x = int(input()) + 1

bin = ""

def f(n):
	global bin
	deci = x
	if deci > (2**n):
		i = str(1)
		deci = deci - (2**n)
	else:
		i = str(0)
	bin = bin + i

j = 64

while j >= 0:
    f(j)
    j = j - 1

print("Converting to binary...")
print(bin)
