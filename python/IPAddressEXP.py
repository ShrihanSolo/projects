#3:48.00

ip = input("Enter IP Address: ") + "."
count = 0
segco = 1
for x in ip:
    if x != ".":
        count += 1
    if x == ".":
        print("Segment "+ str(segco)+ " has " + str(count) + " letters.")
        segco += 1
        count = 0
