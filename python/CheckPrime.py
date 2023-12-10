class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def is_prime(n):
    def prime_helper(k):
        if n == 1:
            return False, 1
        elif k < n and n % k != 0:
            return prime_helper(k+1)
        else:
            return not (k < n), k
    return prime_helper(2)

def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0 or n2 == 0:
        return max(n1, n2)
    elif n1 % 10 < n2 % 10:
        return (n1 % 10) + 10 * (merge(n1 // 10, n2))
    else:
        return (n2 % 10) + 10 * (merge(n1, n2 // 10))

def count_k(n, k):
    if n < 0 or k == 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_k(n-k, k) + count_k(n, k-1)

def hole_number(n):
    if n // 10 == 0:
        return True
    return ((n // 10) % 10) < (n % 10) and ((n // 10) % 10) < ((n // 100) % 10) and hole_number(n // 100)


def min_elements(T, lst):
    """
    >>> min_elements(10, [4, 2, 1]) # 4 + 4 + 2
    3
    >>> min_elements(12, [9, 4, 1]) # 4 + 4 + 4
    3
    >>> min_elements(0, [1, 2, 3])
    0
    """
    if T <= 0:
        return 0 if T == 0 else float('inf')
    return min([min_elements(T - i, lst) for i in lst]) + 1

def generate_subsets():
    """
    >>> subsets = generate_subsets()
    >>> for _ in range(3):
    ...     print(next(subsets))
    ...
    [[]]
    [[], [1]]
    [[], [1], [2], [1, 2]]
    """
    subsets = [[]]
    n = 1
    while True:
        yield subsets
        subsets = subsets + [s + [n] for s in subsets]
        n += 1

def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk.rest == Link.empty:
        return lnk.first
    else:
        return lnk.first + sum_nums(lnk.rest)

def feed(snax, x, y):
    """
    >>> feed([1, 1, 1], 2, 2) # The two robots both refill once at the beginning
    2
    >>> feed([1, 2, 2], 2, 2) # Only one robot refills to feed the middle student
    3
    >>> feed([1, 1, 1, 2, 2], 2, 2)
    4
    >>> feed([3, 2, 1, 3, 2, 1, 1, 2, 3], 3, 3)
    6
    """
    def helper(lst, p, q):
        if p < 0 or q < 0:
            return float("inf")
        elif not lst:
            return 0
        elif len(lst) == 1:
            return not (p >= lst[0] or q >= lst[0])
        else:
            a = helper(lst[1:-1], x - lst[0], y - lst[-1]) + 2
            b = helper(lst[1:-1], p - lst[0], y - lst[-1]) + 1
            c = helper(lst[1:-1], x - lst[0], q - lst[-1]) + 1
            d = helper(lst[1:-1], p - lst[0], q - lst[-1])
            return min(a,b,c,d)
    return helper(snax,0,0)


def insert_in_lnk(lnk, index, value):
    if index > 1:
        return insert_in_lnk(lnk.rest, index - 1, value)
    else:
        x, lnk.rest.first = lnk.rest.first, value
        lnk.rest.rest = Link(x, lnk.rest.rest)
def print_grid(g):
    cs = range(len(g[0]))
    widths = [max([len(str(row[c])) for row in g]) for c in cs]
    for row in g:
        line = ''
        for c in cs:
            s = str(row[c])
            line = line + s + ' ' * (widths[c] - len(s) + 1)
        print(line)

def expand(g, h, w, fill):
    for row in g:
        row.extend([fill for i in range(w-len(row))])
    for k in range(h - len(g)):
        g.extend([[fill for i in range(w)]])

import doctest
doctest.run_docstring_examples(feed, globals(), verbose = True)
