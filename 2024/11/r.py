from functools import cache

@cache
def f(v, n):
  if n == 0:
    return 1

  elif v == 0:
    return f(1, n-1)

  elif len(str(v)) % 2 == 0:
    sv = str(v)
    mid = len(sv) // 2
    v1, v2 = int(sv[:mid]), int(sv[mid:])
    return f(v1, n-1) + f(v2, n-1)

  else:
    return f(2024*v, n-1)

m = list(map(int,open('input.txt').read().split(' ')))

for blinks in [25,75]:
  print(sum(f(v, blinks) for v in m))
