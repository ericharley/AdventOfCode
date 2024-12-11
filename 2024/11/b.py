from collections import defaultdict

line = map(int,open('input.txt').read().split(' '))
m0 = {v:1 for v in line}

def f(m):

  new_m = defaultdict(int)

  for v in m:

    if v == 0:
      new_m[1] += m[v]

    elif len(str(v)) % 2 == 0:
      sv = str(v)
      mid = len(sv) // 2
      v1, v2 = int(sv[:mid]), int(sv[mid:])
      new_m[v1] += m[v]
      new_m[v2] += m[v]

    else:
      new_m[2024*v] += m[v]

  return new_m

for n in [25,75]:
  m = m0
  for _ in range(n):
    m = f(m)

  print( sum(m[v] for v in m) )
