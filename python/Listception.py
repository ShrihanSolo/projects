#print every individual item, in the list that does not contain spam

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "car", "sausage"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])


#for x in menu:
    #if "spam" in x:
        #continue
    #else:
        #for m in x:
            #print(m)

# print(menu)
for i in menu:
    for j in i:
        if j != "spam":
            print j
