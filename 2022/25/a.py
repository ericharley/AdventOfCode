def snafu_to_decimal(line):
  N = len(line)
  m = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
  b = [5**(x-1) for x in list(range(N,0,-1))]

  t = 0
  for x,y in zip(list(line), b):
    t += m[x]*y

  return t

def dec_to_snafu(N):
  o = ''
  m = [0, 1, 2, -2, -1]
  n = {0: '0', 1: '1', 2: '2', 3:'=', 4:'-'}

  while N > 0:
    r = N % 5
    o = n[r] + o
    N = (N - m[r]) // 5

  return o

f = open("input.txt")
t = 0
for line in f.readlines():
  line = line.rstrip()
  t += snafu_to_decimal(line)
  print(line, snafu_to_decimal(line))
 
print(t)
print(dec_to_snafu(t))

