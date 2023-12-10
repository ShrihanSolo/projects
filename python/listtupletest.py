lst = [[1,2], [1], [1,2], [1], [1,2,3]]
x = len(lst)
for i in lst:
    for j in range(0, x):
        if i == lst[j]:
            lst.pop(j)
            x -= 1
print(lst)
