from collections import deque

# Part 1
#
d = deque([0])
k = 1
pos = 0
step = 371

while len(d) <= 2017:
  pos = (pos + step) % len(d)
  d.insert(pos+1,k)
  pos = (pos + 1) % len(d)
  k += 1

print(d[pos+1])

# Part 2
#
d = deque([0])
N = 50*10**6
for i in range(1, N+1):
    d.rotate(-step)
    d.append(i)

print(d[d.index(0)+1])
