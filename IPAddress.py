ipAddress = input("Please enter an IP address: ")

ipAddress += "."
x = 1
y = 0
character = ""

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(x,y))
        x += 1
        y = 0
    else:
        y += 1
