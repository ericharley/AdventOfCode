ss = open('input.txt').read().strip()
t = 0
for s in ss.split(','):
  v = 0
  for ch in s:
    v+= ord(ch)
    v*=17
    v%=256
  t += v
print(t)
