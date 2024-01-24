line = open('input.txt').read().strip()
lens = [ord(c) for c in line] + [17,31,73,47,23]

N = 256
#N = 5
#lens = [3, 4, 1, 5, 17, 31, 73, 47, 23]
ns = list(range(N))
pos = 0
skip = 0

def h(xs):
  t = 0
  for x in xs:
    t ^= x
  return t

def g(i):
  return f'{i:02x}'

for _round in range(64):

 for l in lens:
  idx = list(range(pos,(pos+l)))
  ls = [ns[i%N] for i in idx]
  ls = list(reversed(ls))
  for k,i in enumerate(idx):
    ns[i%N] = ls[k]

  pos = (pos + l + skip ) % N
  skip += 1

output = ''
for i in range(0,256,16):
  output += g(h(ns[i:(i+16)]))
print(output)

#print(ns[0]*ns[1])
