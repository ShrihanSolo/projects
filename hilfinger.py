def hil(hil):
    hil = hil()
    def hil():
        hil = lambda hil: hil
        return hil(hil)
    return hil
hil(lambda: hil)()

def hello(hel):
    x = lambda hel: hel*hel
    return x
print(hello(lambda hel)())
