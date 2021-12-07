import numpy as np

# f = open("test.txt", "r")
f = open("input.txt", "r")
v = [int(x) for x in f.readline().rstrip('\n').split(',')]

a = np.array(v)
c = 0
while True:

  mask = (a == 0)
  a[mask] = 6
  a[~mask] -= 1

  n = np.sum(mask)
  b = 8*np.ones(n, dtype=int)

  a = np.concatenate((a, b))

  c += 1

  if c == 80:
    break

print(c, len(a))
