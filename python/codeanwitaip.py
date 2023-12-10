"""count = 0
for m in ip:
    if m == ".":
        count = count + 1
    else:
        pass
print(count)
ip=23.554.23.432"""


ip = str(input("Enter IP Address: "))
ip = ip + "."
group = ""

for m in ip:
    if m!=".":
        group = group + m
    else:
        print(group)
        group = ""
