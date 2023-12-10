import re

def split(word):
    return [char for char in word]

filter_content = []
content = open(r"RevisedDictionary.txt").read() #CHANGE TO FILE PATH FOR DICTIONARY
content2 = re.findall("(.*?)\n", content)
for j in content2:
    filter_content.append(j.split("  "))
for k in filter_content:
    k.pop()

#letterstr = "tdrpndsnephncrbitegostaag" #egost
#letterstr = "nepsiscmduqnawtwndapci" #tdh
#letterstr = "nepsscmdqnawndapiutci"
#letterstr = "zgtsbtcogrteewhqurdmesras"
letterstr = "kiosble"
#letterstr = "monesneabgtznotywasdpopvr"


capltrstr = split(letterstr.upper())
winlist = []

for word in filter_content:
    i = 0
    capltrstr = split(letterstr.upper())
    for m in word[0]:
        if m in capltrstr:
            capltrstr.remove(m)
            i += 1
            if i == len(word[0]):
                winlist.append(word[0])

winlist.sort(key=len, reverse = True)
for l in winlist[0:50]:
    print(l)
