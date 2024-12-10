line = open('input.txt').read().strip()

m = [int(i) for i in line]

id = 0
out = []
for j,i in enumerate(m):
  if j % 2 == 0:
    out.append([id for _ in range(i)])
    id += 1

  else:
    out.append(list('.'*i))

def compact(m):
  f = [item for row in m for item in row]
  while '.' in f:
    idx = f.index('.')
    f[idx],f[-1] = f[-1],f[idx]
    f.pop()
  return f

def h(s):
  return sum([idx*i for idx,i in enumerate(s)])

print(h(compact(out)))
