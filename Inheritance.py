class hooman:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printer(self):
        print("Good evening, "+ self.fname + " " + self.lname+". It is nice to meet you.")

print("Please enter your first name:")
fn = input()
print("Please enter your last name:")
ln = input()
me = hooman(fn, ln)
me.printer()

class tinyhooman(hooman):
    def __init__(self, fname, lname, age):
        hooman.__init__(self, fname, lname)
        self.age = age

    def doctor(self):
        print("Your doctor's appointment for "+self.fname+" "+self.lname+", aged "+self.age+", has been confirmed. Thank you for your time!")


print("Please enter the tinyhooman's first name:")
fnb = input()
print("Please enter the tinyhooman's last name:")
lnb = input()
print("Please enter the tinyhooman's age:")
age = input()

baby = tinyhooman(fnb, lnb, age)
baby.doctor()
