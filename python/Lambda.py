def g(x):
    return lambda b : b*x
print(g(2))
h = g(2)
i = g(3)
print(h(5))
print(type(i))
