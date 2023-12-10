#This is the part pasted at the start of code
def repeat(loopfunc, num):
    i = 0
    while i < num:
        loopfunc()
        i += 1
    else:
        print("End.")


#This is the code
def imgonnagetlooped():
    print("Hi")
repeat(imgonnagetlooped, 20)
