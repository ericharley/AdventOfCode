import numpy as np
from scipy import stats

with open('input.txt') as f:
#with open('test.txt') as f:
    lines = f.readlines()

n = len(lines[0].rstrip('\n'))
a = np.zeros((1,n)) - 1

for line in lines:
    line = line.rstrip('\n')
    b = np.array([int(x) for x in list(line)], ndmin=2)
    a = np.concatenate((a,b))

a = a[1:,:]

m = stats.mode(a)
l = m.mode[0].tolist()
c = (1 - m.mode[0]).tolist()

s = ''.join([str(int(x)) for x in l])
v = int(s, 2)
print(v)

t = ''.join([str(int(x)) for x in c])
u = int(t, 2)
print(u)

print(v*u)
