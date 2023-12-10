import urllib.request
import re
numbers = 63579
i = 0
while i < 400:
    html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+str(numbers)).read().decode()
    print(html)
    no = re.findall('\d', html)
    numbers = "".join(no)
    print(numbers)
    i += 1
