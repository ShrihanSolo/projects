code = "bcmojJTDnpKNOSVViSLMMyBsoKjV"

import urllib.request
import re


#html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
#lmao = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]

for x in code:
    i = code.index(x)
    print(i)
    if code[i].isupper() and code[i+1].isupper() and code[i+2].isupper() and code[i+3].islower() and code[i+4].isupper() and code[i+5].isupper() and code[i+6].isupper():
        print(code[i:(i+7)], end = '')
    else:
        continue
