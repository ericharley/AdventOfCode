from itertools import accumulate

s = open('input.txt').read()
d = [+1 if ch=='(' else -1 for ch in s]

# Part 1
print(sum(d))

# Part 2
print(list(accumulate(d)).index(-1) + 1)
