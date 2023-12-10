def mergesort(lst):
    lst = [[i] for i in lst]
    if len(lst) == 1:
        return lst
    if (len(lst) % 2 == 0):
        lst = [[min(lst[i][0], lst[i+1][0]) , max(lst[i][0], lst[i+1][0])] for i in range(0, len(lst)-1, 2)]
    else:
        lst = [[min(lst[i][0], lst[i+1][0]) , max(lst[i][0], lst[i+1][0])] for i in range(0, len(lst)-1, 2)]
        lst.append(lst[-1][0])
    return lst


for i in lst:
    if i % 2 == 0:
        i[]
