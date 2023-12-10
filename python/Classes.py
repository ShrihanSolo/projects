#########
class D:
    def __init__ (self, height, width, resolution):
        self.height = height
        self.width = width
        self.resolution = resolution

    def H(self):
        print("The television is " + str(self.height) + "cm tall.")
        print("The television is " + str(self.width) + "cm wide.")
        print("The television has a resolution of " + self.resolution+".")

y = D(30,50,"400ppx")
#print("x =", y.height + y.width)
print(y.height + y.width)
y.resolution = "500ppx"
y.H()
