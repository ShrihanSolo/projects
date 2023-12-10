import re

#INITIALIZATION
filter_content = []
blacklist = []
bracket = []
check = 0
counter = 0 

#PRE-RUN
content = open(r"C:\Users\shrih\OneDrive\Desktop\Shrihan\Python/RevisedDictionary.txt").read()
content2 = re.findall("(.*?)\n", content)
for j in content2:
    filter_content.append(j.split("  "))

#FUNCTIONS
def searchfn(phonetics):
    global counter
    for n in filter_content:
        if phonetics in n[1]:
            if n not in blacklist:
                counter += 1
                blacklist.append(n)
                print(n)

def stressfn(phone):
    for chary in phone:
        if chary in ["0","1","2"]:
            for outputstress in ["0", "1", "2"]:
                    searchfn(phone.replace(chary, str(outputstress)))
        else:
            searchfn(phone)

def simletterfn(splphone, phoney, let1, let2, let3 = "nop", let4 = "nop", let5 = "nop"):
    m = [let1, let2, let3, let4, let5]
    if let5 == "nop":
        m.pop()
    if let4 == "nop":
        m.pop()
    if let3 == "nop":
        m.pop()
    for char in splphone:
        if char in m:
            for letterch in m:
                if letterch != char:
                    letphone = phoney.replace(char, letterch)
                    stressfn(letphone)

def superfn(splphone, phoney):
    stressfn(phoney)
    #AA/AH
    simletterfn(splphone, phoney, "AA0", "AH0")
    simletterfn(splphone, phoney, "AA1", "AH1")
    simletterfn(splphone, phoney, "AA2", "AH2")
    #AE/AY/EY
    simletterfn(splphone, phoney, "EY0", "AE0", "AY0")
    simletterfn(splphone, phoney, "EY1", "AE1", "AY1")
    simletterfn(splphone, phoney, "EY2", "AE2", "AY2")
    #AO/OW
    simletterfn(splphone, phoney, "AO0", "OW0")
    simletterfn(splphone, phoney, "AO1", "OW1")
    simletterfn(splphone, phoney, "AO2", "OW2")
    #CH/SH/S
    simletterfn(splphone, phoney, "S", "SH")
    #x/xH
    simletterfn(splphone, phoney, "T", "TH")
    simletterfn(splphone, phoney, "Z", "ZH")
    simletterfn(splphone, phoney, "D", "DH")

    #OTHER
    simletterfn(splphone, phoney, "V", "W")
    simletterfn(splphone, phoney, "N", "NG")

def duperfn(splphone, phoney):
    stressfn(phoney)
    #AA/AH
    simletterfn(splphone, phoney, "AA0", "AH0")
    simletterfn(splphone, phoney, "AA1", "AH1")
    simletterfn(splphone, phoney, "AA2", "AH2")
    #AE/AY/EY
    simletterfn(splphone, phoney, "EY0", "AE0", "AY0", "EH0", "IH0")
    simletterfn(splphone, phoney, "EY1", "AE1", "AY1", "EH1", "IH1")
    simletterfn(splphone, phoney, "EY2", "AE2", "AY2", "EH2", "IH2")
    #AO/OW
    simletterfn(splphone, phoney, "AO0", "OW0")
    simletterfn(splphone, phoney, "AO1", "OW1")
    simletterfn(splphone, phoney, "AO2", "OW2")
    #CH/SH/S
    simletterfn(splphone, phoney, "S", "SH", "CH", "Z", "ZH")
    #x/xH
    simletterfn(splphone, phoney, "T", "TH")
    simletterfn(splphone, phoney, "D", "DH")
    #OTHER
    simletterfn(splphone, phoney, "V", "W")
    simletterfn(splphone, phoney, "N", "NG")

#USER INTERACTION
while True:
    print("Please enter word to convert to phonetics (or type 'skip' to directly access phonetic search):")
    word = input().upper()

    #PHONETIC WORD SEARCH
    while True:
        if word == "SKIP":
            check += 1
            break
        print("Results Found:")
        for n in filter_content:
            if word == n[0]:
                check += 1
                print(n)

        if check == 0:
            print("None.")
        break

    if check == 0:
        break

    print("Note: You may add brackets around the phonetics you believe may not be required.")
    print("Please enter the order of phonetic letter (with spaces) that you would like to search for:")
    phone = input().upper()
    phoney = phone.replace("(","").replace(")","")

#CALCULATION/OUTPUT
    #BRACKET ITSELF INDEXING/REMOVAL
    splbrackphone = phone.split(" ")
    for char in splbrackphone:
        if "(" in char:
            bracket.append(splbrackphone.index(char))
    splphone = [char.replace("(", "").replace(")", "") for char in splbrackphone]
    superfn(splphone, phoney)

    print(str(counter)+" accurate results found.")
    counter = 0
    print("*******************************")
    #BRAKCETED PHONETIC REMOVED RESULTS
    for index in bracket:
        remchar = splphone[index]
        splphone.pop(index)
        cutphone = " ".join(splphone)
        print(cutphone)
        superfn(splphone, cutphone)
        splphone.insert(index, remchar)

    print(str(counter)+" bracketed results found.")
    counter = 0

    duperfn(splphone, phoney)
    print(str(counter)+" similar results found.")
    print("Task complete.")
    break
