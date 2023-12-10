class Link:
    """A recursive list, with Python integration."""
    empty = None

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + repr(self.rest)
        return 'Link({}{})'.format(self.first, rest)

    def __str__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ' ' + str(self.rest)[2:-2]
        return '< {}{} >'.format(self.first, rest)

class Add:
    s = 2
    def __init__(self, s):
        assert isinstance(s, Link) or s is Link.empty
        self.t = s
        s = self.s + 1
    def this(self, v):
        def f(t):
            if t is Link.empty or t.first >= v:
                return Link(v, t)
            else:
                return Link(t.first, f(t.rest))
        for i in range(self.s):
            self.t = f(self.t)

def multiples(k, n):
    """Yield all positive multiples of k less than n in decreasing order.

    >>> list(multiples(10, 50))
    [40, 30, 20, 10]
    >>> list(multiples(3, 25))
    [24, 21, 18, 15, 12, 9, 6, 3]
    >>> list(multiples(3, 3))
    []
    """
    if k < n:

        for jay in multiples(k, n-k):

            yield jay + k

        yield k
