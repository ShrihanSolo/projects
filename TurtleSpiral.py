import turtle   #Outside_In
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()
skk.speed(0)
skk.color("blue")

turtle.setworldcoordinates(-1,-1,200,200)

def sqrfunc(size):
    for i in range(40):
        skk.fd(size)
        skk.left(90)
        size = size/1.05

sqrfunc(146)
