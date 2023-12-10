import urllib.request
import re
import time

print("Please enter full URL (from study.com):")
link = input()
print("Accessing server...")
content = urllib.request.urlopen(link).read().decode()
print("Decoding resources...")
time.sleep(5)
imp = re.findall("[\"p]>(.*?)</[hp]", content)
bad_chars = ["", "<b>", "</b>", "<i>", "</i>", "<p>","</p>","<h2 id=","</h2>","just create an account.", "You must create an account to continue&nbsp;watching", "Register to view this lesson", "You're on a roll. Keep up the good work!", "Just checking in. Are you still watching?","Want to watch this again later?", "Recommended Lessons and Courses for You"]
print("Filtering unnecessary information...")

while "" in imp:
    imp.remove("")
print(imp)
print("Reformatting...")
for x in imp:
    if "Next Lesson" == x:
        break
    elif "Lesson Objectives" == x:
        break
    elif "Unlock Your Education" == x:
        break
    elif "Learning Outcomes" == x or "Learning Outcome" == x:
        break
    elif "See for yourself why 30 million people use Study.com" == x:
        break
    else:
        for i in bad_chars:
            x = x.replace(i, "")
        x = x.replace("<br />", "\n")
    print(x+"\n")
