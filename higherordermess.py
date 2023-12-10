def adder(i):
    print(i)
    def highadder(j):
        return adder(i+j)
    return highadder
