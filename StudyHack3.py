import urllib.request
import re
import time

#print("Please enter full URL (from study.com):")
#link = input()
link = "https://study.com/academy/answer/is-the-u-s-a-pluralistic-society.html"
print("Accessing server...")
content = urllib.request.urlopen(link).read().decode()
#content = ["<em>No obligation, cancel anytime.</em>", '<em>Select a subject to preview related courses:</em>', 'The answer is friction. <b><span class="textLessonLink"><a class="external" href="https://study.com/academy/lesson/what-is-friction-definition-formula-forces.html">Friction</a></span></b> is a force acting in the opposite direction of motion when two objects come into contact with each other. Without external forces, the car would continue to move west at 65 mph. Now, consider a golfer hitting a ball off the tee. While the ball is on the tee, it is said to be at rest. That is, it has no motion. Once the swinging club comes into contact with the ball, the club applies an external force, disrupts the state of balance and sends the ball flying into motion. ']
print("Decoding resources...")
time.sleep(5)
imp = re.findall("[\"p]>(.*?)</[hp]", content)
#imp = content

zone_chars = ["<a", "<span"]
bad_chars = ["<em>", "</em>", "<b>", "</b>", "<i>", "</i>", "<p>","</p>","<h2 id=","</h2>","just create an account.", "You must create an account to continue&nbsp;watching", "Register to view this lesson", "You're on a roll. Keep up the good work!", "Just checking in. Are you still watching?","Want to watch this again later?", "Recommended Lessons and Courses for You", "No obligation, cancel anytime.", "Select a subject to preview related courses:"]
break_elements = ["Next Lesson", "Lesson Objectives", "Unlock Your Education", "Learning Outcome", "Learning Outcomes", "See for yourself why 30 million people use Study.com"]


replace = False
imp_new = []
for line in imp:
    for bad in bad_chars:
        line = line.replace(bad, "")
    for zone in zone_chars:
        if zone in line:
            for i in line:
                if i == "<":
                    replace = True
                if i == ">":
                    replace = False
                if replace:
                    line = line.replace(i, "")
    imp_new.append(line)

while "" in imp_new:
    imp_new.remove("")

print(imp_new)
for i in imp_new:
    if i in break_elements:
        break
    print(i + "\n")
