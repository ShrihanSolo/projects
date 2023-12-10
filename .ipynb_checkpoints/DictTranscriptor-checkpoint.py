import re
content = open("/Users/Shrihan/Desktop/DictionaryPhonetic.txt").read()
content2 = re.findall("(.*?)\n", content)
filter_content = []
for j in content2:
    filter_content.append(j.split("  "))
dict = re.findall("(.*?)\n", open("/Users/Shrihan/Desktop/DictionaryEnglish.txt").read())
capsdict = []
for n in dict:
    capsdict.append(n.upper())
def fn():
    for m in filter_content:
        if m[0] in capsdict:
            print(m[0]+"  "+m[1])
