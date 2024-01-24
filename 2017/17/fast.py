N = 50*(10**6)
step = 371

pos = 0
out = 0

for k in range(1,N+1):
  pos = (pos + step) % k + 1
  if pos == 1:
    out = k

print(out)
