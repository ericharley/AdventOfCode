from itertools import groupby
from math import prod

data = open('input.txt').read().splitlines()
ops = [{'+': sum, '*': prod}[op] for op in data[-1].split()]

# Part 1
rows = [list(map(int,line.split())) for line in data[:-1]]
cols = [list(col) for col in zip(*rows)]
print( sum(op(terms) for op,terms in zip(ops,cols)) )

# Part 2
cols = [''.join(col) for col in zip(*data[:-1])]
rows = [
    [int(x) for x in group]
    for is_val, group in groupby(cols, key=lambda s: bool(s.strip()))
    if is_val
]
print( sum(op(terms) for op,terms in zip(ops,rows)) )