import time

def repeat(loopfunc, num):
    i = 0
    while i < num:
        loopfunc()
        i += 1
    else:
        print("End.")

floor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
eposn1 = 0
eposn2 = 0

class Elevator:
    while True:
        call = input()
        if call == "end":
            break
        callno = int(call)
        dist1 = abs(callno - eposn1)
        dist2 = abs(callno - eposn2)
        if dist1 > dist2:
            while eposn2 != callno:
                print("Elevator 2 is on floor "+str(eposn2)+".")
                if callno < eposn2:
                    eposn2 -= 1
                elif callno > eposn2:
                    eposn2 += 1
                time.sleep(1)
            else:
                print("Elevator 2 has reached floor "+str(eposn2)+".")
        elif dist1 <= dist2:
            while eposn1 != callno:
                print("Elevator 1 is on floor "+str(eposn1)+".")
                if callno < eposn1:
                    eposn1 -= 1
                elif callno > eposn1:
                    eposn1 += 1
                time.sleep(1)
            else:
                print("Elevator 1 has reached floor "+str(eposn1)+".")
