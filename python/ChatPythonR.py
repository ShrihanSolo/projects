import re
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import numpy as np
import random

# msglist: List of all ['Date, Time, Name, Content']
# data_lst: List of all indexed by [{Date, Time, Name, Content, Number(Num)}]
def chatCleaner(msglist):
    def checkMsg(dex):
        if "-" not in msglist[dex] or ((name1 + ":") not in msglist[dex] and (name2 + ":") not in msglist[dex]):
            msglist[dex-1] = msglist[dex-1] + " " + msglist[dex]
            msglist.pop(dex)
            return checkMsg(dex)
    k = 0
    while k < len(msglist):
        checkMsg(k)
        k += 1
    return msglist

def chatSplter(msglist):
    data_lst = []
    k = 0
    for msg in msglist:
        entry = {}
        data_content_splt = msg.split(" - ", 1)
        date_time_splt = data_content_splt[0].split(", ", 1)
        name_content_splt = data_content_splt[1].split(": ", 1)
        if len(date_time_splt[1]) != 8:
            date_time_splt[1] = "0" + date_time_splt[1]
        entry["Date"], entry["Time"], entry["Name"], entry["Content"], entry["Num"] = date_time_splt[0], convert24(date_time_splt[1]).strip(), name_content_splt[0], name_content_splt[1], k
        data_lst.append(entry)
        k += 1
    return data_lst

def nameLst(name, data = None):
    if data == None:
        data = data_lst
    name_data = [entry for entry in data if entry["Name"] == name]
    return name_data

def wordLst(word, data = None):
    if data == None:
        data = data_lst
    word = word.lower()
    word_data = [[entry, countWordString(word, entry["Content"].lower())] for entry in data if word in entry["Content"].lower()]
    return word_data

def countWordString(word, string):
    return string.count(word)

def printDict(dict):
    for k, v in dict.items():
        print(k, v)

def printList(lst):
    for i in lst:
        print(i)

def randMsgs(data = None):
    if data == None:
        data = data_lst
    k = random.randint(0, len(data_lst) - 1)
    return printList(data_lst[k:k+100])

def convert24(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-3]
    elif str1[-2:] == "AM":
        return str1[:-3]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-3]
    else:
        return str(int(str1[:2]) + 12) + str1[2:5]

def dateKeyer(data = None):
    if data == None:
        data = data_lst
    monthdate_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    start_date, curr_date = data[0]["Date"].split("/"), data[-1]["Date"].split("/")
    try:
        entry_date, curr_date = [int(i) for i in start_date], [int(i) for i in curr_date]
    except ValueError:
        print(start_date, curr_date)
        raise ValueError
    date_dict = {}
    while entry_date[2] <= curr_date[2]:
        while entry_date[0] <= 12:
            while entry_date[1] <= monthdate_dict[entry_date[0]]:
                date = str(entry_date[0]) + "/" + str(entry_date[1]) + "/" + str(entry_date[2])
                date_dict[date] = []
                if entry_date == curr_date:
                    break
                entry_date[1] += 1
            if entry_date == curr_date:
                break
            entry_date[0] += 1
            entry_date[1] = 1
        if entry_date == curr_date:
            break
        entry_date[2] += 1
        entry_date[0] = 1
    return date_dict

def timeKeyer(data = None):
    if data == None:
        data = data_lst
    entry_time = [0, 0]
    time_dict = {}
    while entry_time[0] <= 23:
        while entry_time[1] < 60:
            if len(str(entry_time[1])) == 2:
                mins = str(entry_time[1])
            else:
                mins = str(0) + str(entry_time[1])
            if len(str(entry_time[0])) == 2:
                hrs = str(entry_time[0])
            else:
                hrs = str(0) + str(entry_time[0])
            time = hrs + ":" + mins
            time_dict[time] = []
            entry_time[1] += 1
        entry_time[0] += 1
        entry_time[1] = 0
    return time_dict

def msgSearch(term, typ, data = None):
    if data == None:
        data = data_lst
    for msg in data_lst:
        if term in msg[typ]:
            yield msg



def sortedDateDict(data = None):
    if data == None:
        data = data_lst
    dict = dateKeyer(data)
    for entry in data:
        if entry["Date"] in dict:
            dict[entry["Date"]].append(entry)
        else:
            print("Failed to sort:")
            print(entry)
    return dict

def sortedTimeDict(data = None):
    if data == None:
        data = data_lst
    dict = timeKeyer(data)
    for entry in data:
        if entry["Time"] in dict:
            dict[entry["Time"]].append(entry)
        else:
            print("Failed to sort:")
            print(entry)
    return dict

def dateCount(data = None):
    if data == None:
        data = data_lst
    sort_data = sortedDateDict(data)
    n1 = [len(list(filter(lambda it: it["Name"] == name1, entry))) for entry in list(sort_data.values())]
    n2 = [len(list(filter(lambda it: it["Name"] == name2, entry))) for entry in list(sort_data.values())]
    return n1, n2, [sum(i) for i in list(zip(n1, n2))]

def timeCount(data = None):
    if data == None:
        data = data_lst
    sort_data = sortedTimeDict(data)
    n1 = [len(list(filter(lambda it: it["Name"] == name1, entry))) for entry in list(sort_data.values())]
    n2 = [len(list(filter(lambda it: it["Name"] == name2, entry))) for entry in list(sort_data.values())]
    return n1, n2, [sum(i) for i in list(zip(n1, n2))]

def msgCount(data = None):
    if data == None:
        data = data_lst
    n1 = len(nameLst(name1, data))
    n2 = len(nameLst(name2, data))
    return n1, n2, n1 + n2

def wordCount(word, data = None):
    if data == None:
        data = data_lst
    n1lst, n2lst = wordLst(word, nameLst(name1, data)), wordLst(word, nameLst(name2, data))
    return sum([n1lst[i][1] for i in range(len(n1lst))]), sum([n2lst[i][1] for i in range(len(n2lst))])

def msgCountPrint(data = None):
    if data == None:
        data = data_lst
    print("************************************************")
    n1count, n2count, totcount = msgCount(data)
    print("Total Messages Typed:", totcount)
    print("Messages typed by",  name1 + ":", n1count,  "(" + str(n1count*100/totcount)[:5] + "%)")
    print("Messages typed by",  name2 + ":", n2count, "(" + str(n2count*100/totcount)[:5] + "%)")
    print("************************************************")

def wordCountPrint(word, data = None):
    if data == None:
        data = data_lst
    print("************************************************")
    print("Word:", word.capitalize())
    n1count, n2count = wordCount(word)
    totcount = n1count + n2count
    print("Total Times Used:", totcount)
    print("Times used by",  name1 + ":", n1count, "(" + str(n1count*100/totcount)[:5] + "%)")
    print("Times used by",  name2 + ":", n2count, "(" + str(n2count*100/totcount)[:5] + "%)")
    print("************************************************")


def partFunc(func, interval, data = None):
    if data == None:
        data = data_lst
    result_dict = {}
    k = interval
    while k < len(data):
        part_lst = data[k - interval:k]
        result_dict[k] = func(part_lst)
        k += interval
    return result_dict


def cumlFunc(func, interval, data = None):
    if data == None:
        data = data_lst
    result_dict = {}
    cuml_lst = []
    k = 0
    while k < len(data):
        result_dict[k] = func(cuml_lst)
        k += interval
        cuml_lst = data[:k]
    return result_dict

def wordPlot(word, interval = 2000, data = None):
    print("Processing...")
    if data == None:
        data = data_lst
    plotdict = cumlFunc(lambda data: wordCount(word, data), interval, data)
    xplot, yplot = list(plotdict.keys()), list(plotdict.values())
    n1, n2, tot = [y[0] for y in yplot], [y[1] for y in yplot], [y[0] + y[1] for y in yplot]
    m1, m2 = [0] + [n1[i] - n1[i-1] for i in range(1, len(n1))], [0] + [n2[i] - n2[i-1] for i in range(1, len(n2))]
    mtot = [sum(list(zip(m1, m2))[i]) for i in range(len(m1))]
    printDict(plotdict)
    return plotterLinBar("Usage of '" + word.capitalize() + "'", xplot, [n1, n2, tot], "Cumulative Number of Messages", "Total of '"+ word.capitalize() + "'", y2list = [m1, m2, mtot], y2label = "Change in Messages", pltlabels = [name1, name2, "Total", name1, name2, "Total"])

def datePlot(start = 0, end = 1000000, smoothing = 25, data = None):
    if data == None:
        data = data_lst
    plot_data = sortedDateDict(data[start:end])
    xmarks = list(plot_data.keys())
    xplot = [i for i in range(len(xmarks))]
    n1, n2, tot = dateCount(data[start:end])
    m1, m2, mtot = [0] + [n1[i] - n1[i-1] for i in range(1, len(n1))], [0] + [n2[i] - n2[i-1] for i in range(1, len(n2))], [0] + [tot[i] - tot[i-1] for i in range(1, len(n2))]
    return plotterScatBar("Number of Messages Per Day | Averaged Over " + str(smoothing) + " Days", xplot, [n1, n2, tot], "Date", "Number of Messages", y2list = [m1, m2, mtot], y2label = "Daily Change", pltlabels = [name1, name2, "Total", name1, name2, "Total"], cut = 0, smoothing = smoothing, xmarks = xmarks)

def timePlot(start = 0, end = 1000000, smoothing = 60, data = None):
    if data == None:
        data = data_lst
    plot_data = sortedTimeDict(data[start:end])
    xmarks = list(plot_data.keys())
    xplot = [i for i in range(1440)]
    n1, n2, tot = timeCount(data[start:end])
    m1, m2, mtot = [0] + [n1[i] - n1[i-1] for i in range(1, len(n1))], [0] + [n2[i] - n2[i-1] for i in range(1, len(n2))], [0] + [tot[i] - tot[i-1] for i in range(1, len(n2))]
    return plotterScatBar("Number of Messages Per Minute | Averaged Over " + str(smoothing) + " Minutes", xplot, [n1, n2, tot], "Time", "Number of Messages", y2list = [m1, m2, mtot], y2label = "Change by Minute", pltlabels = [name1, name2, "Total", name1, name2, "Total"], cut = 20, nth = 20, smoothing = smoothing, xmarks = xmarks)

def lenMsgCount(data = None):
    if data == None:
        data = data_lst
    n1msg, n2msg, totmsg = msgCount(data)
    n1char, n2char = wordCount("", data)
    totchar = n1char + n2char
    return (n1char-n1msg)/n1msg, (n2char-n2msg)/n2msg, (totchar-totmsg)/totmsg

def lenMsgPlot(interval = 2000, cut = 12, data = None):
    print("Processing...")
    if data == None:
        data = data_lst
    plotdict = partFunc(lenMsgCount, interval, data)
    xplot, yplot = list(plotdict.keys()), list(plotdict.values())
    n1, n2, tot = [y[0] for y in yplot], [y[1] for y in yplot], [y[2] for y in yplot]
    m1, m2, mtot = [0] + [n1[i] - n1[i-1] for i in range(1, len(n1))], [0] + [n2[i] - n2[i-1] for i in range(1, len(n2))], [0] + [tot[i] - tot[i-1] for i in range(1, len(n2))]
    #for i in list(zip(xplot, n1, n2, tot)):
        #print(i)
    return plotterScatBar("Average Message Length Over Time", xplot, [n1, n2, tot], "Cumulative Number of Messages", "Average Character Length", y2list = [m1, m2, mtot], y2label = "Change in Average", pltlabels = [name1, name2, "Total", name1, name2, "Total"], cut = cut, smoothing = 25)

def plotterLinBar(title, xlist, ylist, xlabel, ylabel, y2list = None, y2label = None, pltlabels = None, pltcolors = [(144,103,167), (225,151,76), (114,147,203), (144,103,167), (225,151,76), (114,147,203)], alpha = 0.45, bounds = None):
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    pltcolors = tuple([[no/255 for no in list(col)] for col in pltcolors])
    if y2list:
        plt2colors = [tuple(list(col) + [alpha]) for col in pltcolors[3:]]
        totw = (xlist[1] - xlist[0])
        w = (totw/len(y2list))/1.33
        s = -(totw/2)
        for i in range(len(y2list)):
            ax.bar([s + i for i in xlist], y2list[i], width = w, color = plt2colors[i], label = pltlabels[i+len(ylist)], zorder = 0)
            s += w
        ax.set_xlabel(xlabel)
        ax.set_ylabel(y2label)
    for i in range(len(ylist)):
        ax2.plot(xlist, ylist[i], color = pltcolors[i], label = pltlabels[i], linewidth = 3, zorder = 10)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel)
    if bounds:
        plt.xlim(bounds)
    plt.legend(loc = "upper left")
    plt.title(title)
    print("Complete.")
    plt.show()

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


def plotterScatBar(title, xlist, ylist, xlabel, ylabel, y2list = None, y2label = None, pltlabels = None, pltcolors = [(144,103,167), (225,151,76), (114,147,203), (144,103,167), (225,151,76), (114,147,203)], alpha = 0.45, bounds = None, cut = 0, smoothing = 25, xmarks = [], nth = 4):
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    pltcolors = tuple([[no/255 for no in list(col)] for col in pltcolors])
    if y2list:
        plt2colors = [tuple(list(col) + [alpha]) for col in pltcolors[3:]]
        totw = (xlist[1] - xlist[0])
        w = (totw/len(y2list))/1.33
        s = -(totw/2)
        for i in range(len(y2list)):
            ax.bar([s + i for i in xlist], y2list[i], width = w, color = plt2colors[i], label = pltlabels[i+len(ylist)], zorder = 0)
            s += w
        ax.set_xlabel(xlabel)
        ax.set_ylabel(y2label)
    for i in range(len(ylist)):
        ax2.scatter(xlist, ylist[i], s = 15, color = pltcolors[i], label = pltlabels[i])
        ax2.plot(xlist[cut:len(xlist)-cut], smooth(ylist[i], smoothing)[cut:len(xlist)-cut], linewidth = 3, color = pltcolors[i], label = pltlabels[i])
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel)
    if xmarks:
        plt.xticks(xlist[::10], xmarks[::10])
        every_nth = nth
        for n, label in enumerate(ax.xaxis.get_ticklabels()):
            if n % every_nth != 0:
                label.set_visible(False)
        ax.tick_params(axis = 'x', rotation = 45)
    if bounds:
        plt.xlim(bounds)
    plt.legend(loc = "upper left")
    plt.title(title)
    print("Complete.")
    plt.show()

#ENTRY VALUES
## Who is the chat between? Enter WITH QUOTES
name1 = "Shrihan Agarwal"
name2 = "Vismaya Pillai"
print("Loading Data...")
## What is the path to the chat file? Replace (and keep the r!):
content = open(r"/Users/shri/Documents/DocumentsMain/Shrihan/Export/VPC2022.txt", encoding = "utf8").read()
msglist = re.findall("(.*?)\n", content[0:])
data_lst = chatSplter(chatCleaner(msglist))
print("Complete.")
print("*******************************************************")
print("List of Functions:")
print("- msgCountPrint()")
print("- wordCountPrint(word)")
print("- lenMsgCount()")
print("- wordPlot(word, interval = 2000)")
print("- datePlot(start = 0, end = 1000000, smoothing = 25)")
print("- timePlot(start = 0, end = 1000000, smoothing = 60)")
print("- lenMsgPlot(interval = 2000, cut = 12)")
print("*******************************************************")

#wordPlot("🤦🏻‍♀")
#wordPlot("🤦🏻‍♂")
