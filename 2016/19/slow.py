from collections import deque

d = deque(range(1,3018458+1))

n = len(d)
while n > 1:
  r = n // 2
  d.rotate(-r)
  d.popleft()
  d.rotate(r-1)
  n -= 1

print(d[0])
