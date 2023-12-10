a = ""
c = 1
p = input("Enter IP address: ")
ip = str(p)
for i in ip:
    if i == ".":
        print("segment", c, "has", len(a), "characters")
        a = ""
        c = c+1

    elif i == ip[-1]:
        print("segment", c, "has", len(a)+1, "characters")
    else:
        a = a + i
