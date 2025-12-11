c = 0
t = 50
lines = open('input.txt').readlines()
for line in lines:
  line = line.strip()
  n = int(line[1:])
  d = line[0]
  if d == 'R':
    for _ in range(n):
      t += 1
      if t % 100 == 0:
        c += 1
  else:
    for _ in range(n):
      t -= 1
      if t % 100 == 0:
        c += 1

print(c)