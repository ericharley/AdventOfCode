t0, data = open('input.txt').read().strip().split('\n')
t0 = int(t0)
data = data.split(',')
data = [int(_) for _ in data if _ != 'x']

for x in range(max(data)):
  for m in data:
    if (t0 + x) % m == 0:
      print(x*m)
      exit()
