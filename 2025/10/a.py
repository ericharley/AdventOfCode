def s2i(s):
  return int(s[::-1].replace('#', '1').replace('.', '0'), 2)

def b2i(bits):
  return sum(1 << b for b in bits)

t = 0
lines = open('input.txt').read().strip().splitlines()
for line in lines:
  f = line.split()
  target = s2i(f[0].replace('[','').replace(']',''))
  buttons = [ b2i(eval(b[:-1]+',)')) for b in f[1:-1]]

  s = set([0])
  while target not in s:
    s = { a^b for a in s for b in buttons }
    t += 1 

print(t)
