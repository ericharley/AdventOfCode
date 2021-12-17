import numpy as np

a = np.genfromtxt('./input.txt', delimiter=1, dtype=int)

b = np.copy(a)
n = np.shape(b)[0]
i = 0
while n > 1:
 if np.sum(b[:,i] == 0) > np.sum(b[:,i] == 1):
   # 0 most common
   b = b[b[:,i] == 0]
 else:
   # 1 most common
   b = b[b[:,i] == 1]
 n = np.shape(b)[0]
 i += 1

#c = b[0].tolist()
#t = ''.join([str(int(x)) for x in c])
#u = int(t, 2)

# u = np.sum( (2*b[0]) ** np.flip(np.arange(len(b[0]))) )
b = b[0]
u = b.dot(2**np.arange(len(b))[::-1])

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

l = b[0].tolist()
s = ''.join([str(int(x)) for x in l])
v = int(s, 2)

# v = np.power(x2,np.flip(x1))

print(v*u)
