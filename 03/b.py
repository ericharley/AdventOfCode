import numpy as np
from scipy import stats

#with open('input.txt') as f:
with open('test.txt') as f:
    lines = f.readlines()

n = len(lines[0].rstrip('\n'))
a = np.zeros((1,n)) - 1

for line in lines:
    line = line.rstrip('\n')
    b = np.array([int(x) for x in list(line)], ndmin=2)
    a = np.concatenate((a,b))

a = a[1:,:]

b = np.copy(a)
n = np.shape(b)[0]
o = []
i = 0
while n > 1:
 if np.sum(b[:,i] == 0) > np.sum(b[:,i] == 1):
   # 0 most common
   b = b[b[:,i] == 0]
   o += [0]
 else:
   # 1 most common
   b = b[b[:,i] == 1]
   o += [1]
 n = np.shape(b)[0]
 i += 1
 #print(n)

print(b)
c = b[0].tolist()

b = np.copy(a)
n = np.shape(b)[0]
i = 0
while n > 1:
 if np.sum(b[:,i] == 0) <= np.sum(b[:,i] == 1):
   # 1 least common
   b = b[b[:,i] == 0]
 else:
   # 0 least common
   b = b[b[:,i] == 1]
 n = np.shape(b)[0]
 i += 1
 #print(n)

print(b)
l = b[0].tolist()

print(c)
print(l)

s = ''.join([str(int(x)) for x in l])
v = int(s, 2)
print(v)

t = ''.join([str(int(x)) for x in c])
u = int(t, 2)
print(u)

print(v*u)
