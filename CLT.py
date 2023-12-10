import random
import matplotlib.pyplot as plt
import statistics as st

dist1 = [1,1,1,2,3,3,4,4,4,4,5,5,6,6,6,6,6,7,7,7,8,8,8,8,9,9,10,10,10,10]
mn = st.mean(dist1)
sdev = st.stdev(dist1)
no = 2
samp = 1000

freqMn = []
noCo = []
freqMnC = []

def distFn(no, samp, dist = dist1):
    mnset = []
    j = 0
    while j < samp:
        chset = []
        i = 0
        while i < no:
            chset.append(random.choice(dist))
            i += 1
        mn = st.mean(chset)
        mnset.append(mn)
        j += 1
    distset = set(mnset)
    distset = list(distset)
    distset.sort()
    freqset = []
    for i in distset:
        freqset.append(mnset.count(i))
    histset = []
    for i in range(0, len(distset)):
        histset.append([distset[i], freqset[i]])
    pmnset = []
    for i in range(0, len(distset)):
        pmnset.append(distset[i]*freqset[i])
    mnFn = sum(pmnset) / sum(freqset)
    #plt.hist(mnset, bins = "auto", color = "#0504aa", alpha = 0.7, rwidth = 0.85)
    #plt.grid(axis = "y", alpha = 0.75)
    #plt.xlabel("Numbers")
    #plt.ylabel("Frequency")
    #plt.title("Frequency Distribution for (" + str(no) + "," +str(samp) + ")")
    #plt.show()
    freqMn.append(mnFn)
    noCo.append(no)

k = 2
while k < 200:
    distFn(k, samp)
    k += 1
for i in range (0, len(noCo)):
    freqMnC.append(mn)
plt.plot(noCo, freqMn, label = "Approaching Mean")
plt.plot(noCo, freqMnC, label = "Mean")
plt.xlabel("Number (n)")
plt.ylabel("Mean")
plt.title("Mean, With Increasing n")
plt.show()
