N = 50*(10**6)
next = [0]*(N+1)

cur = 0
next[0] = 0

k = 1
step = 371

for k in range(1, N+1):
  for _ in range(step):
    cur = next[cur]
  next[cur], next[k] = k, next[cur]
  cur = k

print(next[0])
