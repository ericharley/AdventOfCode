from collections import defaultdict

data = [11,18,0,20,1,7,16]

def doit(d,n):
  said = defaultdict(list)

  for i,v in enumerate(d):
    said[v] = [i+1]
    last_spoken = v

  for i in range(len(d)+1, n + 1):
    t = said[last_spoken]

    if len(t) == 1:
      last_spoken = 0
    else:
      last_spoken = t[-1] - t[-2]

    said[last_spoken].append(i)

  print(d, last_spoken)

Ns = [2020, 30000000]

for N in Ns:
  doit(data,N)
