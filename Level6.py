import zipfile
import re


num = 90052
comments = []
i = 0
while i < 4000:
    f = open("/Users/Shrihan/Downloads/channel/"+str(num)+".txt")
    content = f.read()
    comments.append(f.getinfo(num+".txt").decode("utf-8"))
    a = re.findall('\d', content)
    num = "".join(a)
    print(content)
    print(num)
    i += 1
