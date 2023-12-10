import re
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy import interpolate

#ENTRY VALUES
#Who is the chat between? Enter WITH QUOTES
name1 = "Shrihan Agarwal"
name2 = "Vismaya Pillai"
#What is the path to the chat file? Replace (and keep the r!):
content = open(r"C:\Users\shrih\OneDrive\Desktop/VPC2020.txt", encoding = "utf8").read()

" IGNORE ALL THIS, SKIP TO END, AFTER THIS LINE APPEARS AGAIN :) "
#________________________________________________________________________________

#INITIALIZATION
countshri = 0
countvisu = 0
mediacount = 0
chatter1 = name1 + ":"
chatter2 = name2 + ":"
sdatecount = 0
vdatecount = 0
datecount = 0
datefreq = []
datelistx = []
datelisty = []
datelistvy = []
datelistsy = []
timefreq = []
stimecount = 0
vtimecount = 0
timecount = 0
timelistx = []
timelisty = []
timelistvy = []
timelistsy = []
minutelisty = []


#DEFINING FUNCTIONS
def convert24(str1):

    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:

        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]

def ChatCleaner():
    for j in content2:
        if chatter1 in j:
            continue
        elif chatter2 in j:
            continue
        else:
            posn = content2.index(j)
            content2[(posn - 1) : (posn+1)] = [''.join(content2[(posn - 1) : (posn+1)])]

def SuperChatCleaner():
    print("Ejecting Unnecessary Data...")
    ChatCleaner()
    #time.sleep(0.5)
    print("10% Done...")
    ChatCleaner()
    #time.sleep(0.5)
    print("20% Done...")
    ChatCleaner()
    #time.sleep(0.5)
    print("30% Done...")
    ChatCleaner()
    #time.sleep(0.5)
    print("40% Done...")
    ChatCleaner()
    #time.sleep(0.5)
    print("50% Done...")
    ChatCleaner()
    #time.sleep(0.5)
    print("60% Done...")
    ChatCleaner()
    #time.sleep(0.5)
    print("70% Done...")
    ChatCleaner()
    #time.sleep(0.5)
    print("80% Done...")
    ChatCleaner()
    #time.sleep(0.5)
    print("90% Done...")
    ChatCleaner()
    #time.sleep(0.5)
    print("Done.")

def MessageCounter():
    print("Calculating Number/Ratio of Messages Sent...")
    countshri = 0
    countvisu = 0
    for j in content2:
        jlen = len(j)
        counter1 = j.count(chatter1, 1, jlen)
        counter2 = j.count(chatter2, 1, jlen)
        countshri = countshri + counter1
        countvisu = countvisu + counter2
    #time.sleep(2)
    print("Done.")
    print(name1+ " has typed " + str(countshri) + " messages.", "(" + str((countshri/(countvisu+countshri))*100) + ")")
    print(name2 + " has typed " + str(countvisu) + " messages.", "(" + str((countvisu/(countvisu+countshri))*100) + ")")
    print("Total Messages Typed = " + str(countshri+countvisu))
    print("*********************************************************************")

def WordCounter(word, output):
    print("Calculating Occurrences of '" + output + "' in Chat...")
    wcount = 0
    scount = 0
    vcount = 0
    ucount = 0
    for j in content2:
        jlen = len(j)
        counterS = 0
        counterV = 0
        counterU = 0
        counter1 = j.lower().count(word, 1, jlen)
        if counter1 > 0:
            counterS = j.count(chatter1, 1, jlen)
            counterV = j.count(chatter2, 1, jlen)
        if counterS == 0 and counterV == 0 and counter1 > 0:
                counterU = counter1
        wcount = wcount + counter1
        scount = scount + counterS*(counter1)
        vcount = vcount + counterV*(counter1)
        ucount = ucount + counterU
    #time.sleep(1)
    print("Done.")
    print("Number of times", "'"+ output + "'", "found:", str(wcount))
    print("Number of times sent by " + chatter1, str(scount), "(" + str((scount/(vcount+scount))*100) + ")")
    print("Number of times sent by " + chatter2, str(vcount), "(" + str((vcount/(vcount+scount))*100) + ")")
    print("Sent but by whom unknown (?):", str(ucount))
    print("*********************************************************************")

def WordPlotter(word, name):
    print("Plotting Frequency of '" + name + "' by Day...")
    sdatecount = 0
    vdatecount = 0
    datecount = 0
    datelistx = []
    datelisty = []
    datelistvy = []
    datelistsy = []
    whitelist = ["8/27/19"]

    wordfreq = []
    for delement in superchat:
        if len(delement) == 4:
            if word in delement[3].lower():
                if "/19" in delement[0]:
                    listy = []
                    listy.append(delement[0])
                    listy.append(delement[2])
                    wordfreq.append(listy)
                if "/20" in delement[0]:
                    listy = []
                    listy.append(delement[0])
                    listy.append(delement[2])
                    wordfreq.append(listy)

    for date in wordfreq:
        if date[0] in whitelist:
            if date[1] == name1:
                sdatecount += 1
            elif date[1] == name2:
                vdatecount += 1
            datecount += 1
        else:
            datelistx.append(whitelist[-1])
            datelisty.append(datecount)
            datelistsy.append(sdatecount)
            datelistvy.append(vdatecount)
            whitelist.append(date[0])
            datecount = 0
            sdatecount = 0
            vdatecount = 0
    datelistx.append(whitelist[-1])
    datelisty.append(datecount)
    datelistsy.append(sdatecount)
    datelistvy.append(vdatecount)
    whitelist.append(date[0])
    plt.plot(datelistx, datelisty, label = "Total")
    plt.plot(datelistx, datelistsy, label = name1)
    plt.plot(datelistx, datelistvy, label = name2)
    plt.xlabel('Date')
    plt.ylabel('Number of Messages')
    plt.title(name + ' Word Usage Amount By Day Shri/Visu')
    plt.show()
    print("Done.")

def datefreqCreator():
    print("Creating Sample Set of Message Frequencies Per Day...")
    #DATE FREQUENCY/LIST OF ALL DATES
    for delement in superchat:
        if "/19" in delement[0]:
            listy = []
            listy.append(delement[0])
            listy.append(delement[2])
            datefreq.append(listy)
        if "/20" in delement[0]:
            listy = []
            listy.append(delement[0])
            listy.append(delement[2])
            datefreq.append(listy)
    #time.sleep(1)
    print("Done.")

def datefreqCleaner():
    global datelistx
    global datelisty
    global datelistsy
    global datelistvy
    print("Filtering Sample Set of Message Frequencies Per Day...")
    datecount = 0
    sdatecount = 0
    vdatecount = 0
    whitelist = ["8/27/19"]
    for date in datefreq:
        if date[0] in whitelist:
            if date[1] == name1:
                sdatecount += 1
            elif date[1] == name2:
                vdatecount += 1
            datecount += 1
        else:
            datelistx.append(whitelist[-1])
            datelisty.append(datecount)
            datelistsy.append(sdatecount)
            datelistvy.append(vdatecount)
            whitelist.append(date[0])
            datecount = 0
            sdatecount = 0
            vdatecount = 0
    datelistx.append(whitelist[-1])
    datelisty.append(datecount)
    datelistsy.append(sdatecount)
    datelistvy.append(vdatecount)
    whitelist.append(date[0])
    """for i in list(zip(datelistx, datelisty)):
        print(i)"""
    """def smoother(datelist):
        for i in range(0, len(datelist) - 31):
            j = len(datelist) - i - 1
            datelist[j] = sum([datelist[j - n] for n in range(0, 31)])
        return datelist[31:]
    datelistx = datelistx[31:]
    datelisty = smoother(datelisty)
    datelistsy = smoother(datelistsy)
    datelistvy = smoother(datelistvy)"""
    #time.sleep(1)
    print("Done.")

def datefreqPlotter():
    print("Plotting Filtered Sample Set of Message Frequencies Per Day...")
    plt.plot(datelistx, datelisty, label = "Total")
    plt.plot(datelistx, datelistsy, label = name1)
    plt.plot(datelistx, datelistvy, label = name2)
    plt.tick_params(axis ='x', rotation = 45)
    plt.xticks(np.arange(0, len(datelistx), 5))
    plt.xlabel('Date')
    plt.ylabel('Number of Messages')
    plt.title('Chat Amount By Day Shri/Visu')
    plt.show()
    #time.sleep(1)
    print("Done.")

def DateFrequency():
    datefreqCreator()
    datefreqCleaner()
    datefreqPlotter()

def timefreqCreator():
    print("Creating Sample Set of Message Frequencies Per Minute of Day...")
    for delement in superchat:
        if "/19" in delement[0]:
            if len(delement[1]) == 7:
                delement[1] = str(0)+delement[1]
            listy = []
            listy.append(convert24(delement[1]))
            if " PM" in listy[0]:
                listy[0] = listy[0].replace(" PM", "")
            if " " in listy[0]:
                listy[0] = listy[0].replace(" ", "")
            listy.append(delement[2])
            timefreq.append(listy)
        if "/20" in delement[0]:
            if len(delement[1]) == 7:
                delement[1] = str(0)+delement[1]
            listy = []
            listy.append(convert24(delement[1]))
            if " PM" in listy[0]:
                listy[0] = listy[0].replace(" PM", "")
            if " " in listy[0]:
                listy[0] = listy[0].replace(" ", "")
            listy.append(delement[2])
            timefreq.append(listy)
    timefreq.sort()
    #time.sleep(1)
    print("Done.")

def timefreqCleaner():
    print("Filtering Sample Set of Message Frequencies Per Minute of Day...")
    minutelist = ["0000"]
    timecount = 0
    stimecount = 0
    vtimecount = 0

    while int(minutelist[-1][0] + minutelist[-1][1]) < 24:
        if int(minutelist[-1][-2] + minutelist[-1][-1]) == 59:
            minutelist.append(str(int(minutelist[-1]) + 100 - 59))
            while len(minutelist[-1]) < 4:
                minutelist[-1] = str(0)+minutelist[-1]
        elif int(minutelist[-1][-2] + minutelist[-1][-1]) < 59:
            minutelist.append(str(int(minutelist[-1]) + 1))
            while len(minutelist[-1]) < 4:
                minutelist[-1] = str(0)+minutelist[-1]

    for time in minutelist:
        time = time[0:2] + ":" + time[2:4]
        minutelisty.append(time)

    for minute in minutelisty:
        for time in timefreq:
            if minute == time[0]:
                if time[1] == name1:
                    stimecount += 1
                elif time[1] == name2:
                    vtimecount += 1
                timecount += 1
        timelisty.append(timecount)
        timecount = 0
        timelistsy.append(stimecount)
        stimecount = 0
        timelistvy.append(vtimecount)
        vtimecount = 0
    timelisty[-1] = timelisty[0]
    timelistvy[-1] = timelistvy[0]
    timelistsy[-1] = timelistsy[0]
    print("Done.")

def timefreqPlotter():
    print("Plotting Filtered Sample Set of Message Frequencies Per Minute of Day...")
    plt.plot(minutelisty, timelisty, label = "Total")
    plt.plot(minutelisty, timelistsy, label = name1)
    plt.plot(minutelisty, timelistvy, label = name2)
    plt.tick_params(axis ='x', rotation = 45)
    plt.xticks(np.arange(0000, 2400, 60))
    plt.xlim((-60, 1500))
    plt.xlabel('Time')
    plt.ylabel('Number of Messages')
    plt.title('Chat Amount By Minute ' + name1 + "/" + name2)
    plt.show()
    print("Done.")

def TimeFrequency():
    timefreqCreator()
    timefreqCleaner()
    timefreqPlotter()

#CREATING SUPERCHAT
print("UTF-8 Decoding WhatsApp Chat to Readable Format...")
content2 = re.findall("(.*?)\n", content)
superchat = []
for k in content2:
    dateelement = []
    for m in k.split(' - '):
        if "/19" in m:
            for n in m.split(', '):
                dateelement.append(n)
        elif "/20" in m:
            for n in m.split(', '):
                dateelement.append(n)
        else:
            for n in m.split(': '):
                dateelement.append(n)
    superchat.append(dateelement)
#time.sleep(2)
print("Done.")

#PRE-RUN
SuperChatCleaner()

#________________________________________________________________________________

"WELCOME BACK! HERE IS WHERE YOU DECIDE WHAT YOU WANNA RUN - REMOVE THE # TO ACTIVATE THEM!"

"MESSAGECOUNTER() COUNTS THE TOTAL MESSAGES, AND THE RATIOS OF TOTAL MESSAGES SENT"
MessageCounter()

"ENTER LIST OF WORDS TO SEARCH FOR AND COMPARE USAGE OVERALL - IN LOWERCASE, THEN THE DESCRIPTION/LABEL"
counterList = [["cyut", "Cyut"], ["cute","Cute"], ["<media omitted>", "Media"], ["kiddo", "Kiddo"], ["bye", "Bye"], ["omg", "OMG"], ["wtf", "WTF"], ["😂", "Laughy Emoji"], ["😭", "Cry Emoji"], ["🤦🏻‍♂", "Facepalm Emoji - Male"], ["🤦🏻‍♀", "Facepalm Emoji - Female"], ["the ", "The"]]
for word in counterList:
    WordCounter(word[0], word[1])
    continue

"DATEFREQUENCY() GIVES YOU A PLOT OF CHAT AMOUNT PER DAY OVER TOTAL TIME"
DateFrequency()

"ENTER LIST OF WORDS TO PLOT AND COMPARE USAGE OVER TIME - IN LOWERCASE, THEN THE DESCRIPTION/LABEL"
plotterList = [["cyut", "Cyut"], ["cute","Cute"], ["<media omitted>", "Media"], ["kiddo", "Kiddo"], ["bye", "Bye"], ["omg", "OMG"], ["wtf", "WTF"], ["😂", "Laughy Emoji"], ["😭", "Cry Emoji"], ["🤦🏻‍♂", "Facepalm Emoji - Male"], ["🤦🏻‍♀", "Facepalm Emoji - Female"], ["the ", "The"], ["😇", "Angel Emoji"]]
for word in plotterList:
    WordPlotter(word[0], word[1])
    continue


"TIMEFREQUENCY() GIVES YOU A PLOT OF CHAT FREQUENCY BASED ON TIME OF DAY (TAKES A BIT OF TIME TO LOAD)"
TimeFrequency()
