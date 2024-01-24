line = open('input.txt').read().strip().replace(',',' ').split()
lens = list(map(int,line))

N = 256
ns = list(range(N))
pos = 0
skip = 0

for l in lens:
  idx = list(range(pos,(pos+l)))
  ls = [ns[i%N] for i in idx]
  ls = list(reversed(ls))
  for k,i in enumerate(idx):
    ns[i%N] = ls[k]

  pos = (pos + l + skip ) % N

  skip += 1


print(ns[0]*ns[1])
