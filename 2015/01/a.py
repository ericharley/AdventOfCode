from itertools import accumulate

lines = open('input.txt').read().splitlines()
d = [+1 if ch=='(' else -1 for line in lines for ch in line]

print(sum(d))
print(list(accumulate(d)).index(-1) + 1)
