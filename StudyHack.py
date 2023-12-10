import urllib.request
import re

print("Accessing server...")
content = urllib.request.urlopen("https://study.com/academy/lesson/the-metric-system-units-and-conversion.html").read().decode()
print("Decoding resources...")
imp = re.findall(">(.*?)</[hp]", content)

bad_chars = ["<b>", "</b>", "<i>", "</i>", "<p>","</p>","<h2 id=","</h2>","just create an account.","\"section---", "\">", "You must create an account to continue&nbsp;watching", "Register to view this lesson", "You're on a roll. Keep up the good work!", "Just checking in. Are you still watching?","Want to watch this again later?", "Recommended Lessons and Courses for You"]
print("Filtering unnecessary information...")
print("Reformatting...")
for x in imp:
    if "<span" in x:
        continue
    if "em>" in x:
        continue
    elif "Unlock Your Education" == x:
        break
    else:
        for i in bad_chars:
            x = x.replace(i, "")
            x = x.replace("Unlock Content", "THE FOLLOWING IS LOCKED CONTENT:")
        print(x+"\n")
