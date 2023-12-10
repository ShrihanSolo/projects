""""arrb6???4xxbl5???eee5" => true
"acc?7??sss?3rr1??????5" => true
"5??aaaaaaaaaaaaaaaaaaa?5?5" => false
"9???1???9???1???9" => true
"aa6?9" => false"""
x = input("Add your own test (Enter 'no' if you just want to see tests): ")
allstr = ["arrb6???4xxbl5???eee5", "acc?7??sss?3rr1??????5", "5??aaaaaaaaaaaaaaaaaaa?5?5", "9???1???9???1???9", "aa6?9", x]
if x.lower() == "no":
    allstr.pop()
lst = []
count = 0
cont = 1
exist = 0
for n in allstr:
    print(n)
    for m in n:
        if m == "?":
            count += 1
        if m.isnumeric() == True:
            lst.append([m, count])
            count = 0
    for m in range(0, len(lst)-1):
        if (int(lst[m][0]) + int(lst[m+1][0])) == 10:
            if lst[m+1][1] == 3:
                exist = 1
                pass
            else:
                cont = 0
    lst = []
    if cont == 1:
        if exist == 1:
            print("True!")
        else:
            print("False!")
    elif cont == 0:
        print("False!")
    cont = 1
    exist = 0
