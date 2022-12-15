import re

s = []

x = open(0)
for line in x:
    if line == "\n":
      break
    s.append(list(line[1::4])) 

s.pop()
s = [list("".join(c).strip()[::-1]) for c in zip(*s)]

for line in x:
    a, b, c = map(int, re.findall("\\d+", line))
    for i in range(a):
      s[c-1].append( s[b-1].pop() )

print( ''.join([x[-1] for x in s]) )

