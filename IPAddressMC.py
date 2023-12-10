a = ""
c = 1
p = input("Enter IP address: ")
ip = str(p)
for i in ip:
    if i == ".":
        print("segment", c, "has", len(a), "characters")
        a = ""
        c = c+1
    else:
        a = a + i
