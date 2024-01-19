import math

def f(n):
  k = math.floor(math.log(n,3))

  if (n == 3**k):
    return n

  if n%2==1 and (n+1)//2 == 3**k:
    return (n + 1)/2-1
  if n%2==0 and (n+1)//2 == 3**k:
    return (n )/2

  o = 0
  for i in range((3**k)+1, (3**k)*2-1):
    o += 1
    if i == n:
      return o
  for i in range((3**k)*2, 3**(k+1)):
    o += 2
    if i == n:
      return o
  return o

from collections import deque

for i in range(1,1000):
  d = deque(range(1,i+1))

  n = len(d)
  while n > 1:
    r = n // 2
    d.rotate(-r)
    d.popleft()
    d.rotate(r-1)
    n -= 1

  if d[0] != f(i):
    print(i, d[0], f(i))

