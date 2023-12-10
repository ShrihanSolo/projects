class MyEvenNumber:
    def __init__(self):
        self.a = 2
        b = 4
        print(b)
        print("Initializing")

    def __iter__(self):
        return self

    def __next__(self):
        x = self.a
        print(b)
        print(x)
        self.a += 2
        print(x)
        return self.a



myEvenObject = MyEvenNumber()
ptr = iter(myEvenObject)
print(next(ptr))
