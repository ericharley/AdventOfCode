import re

s = []

x = open(0)

for line in x:
    if line == "\n": break
    s.append([line[k * 4 + 1] for k in range(len(line) // 4)]) # this is just line[1::4] - thanks UnrelatedString

s.pop()
s = [list("".join(c).strip()[::-1]) for c in zip(*s)]

for line in x:
    a, b, c = map(int, re.findall("\\d+", line))
    t = []
    for i in range(a):
      t.append(s[b-1].pop())
    for i in range(a):
      s[c-1].append(t.pop())

print(''.join([x[-1] for x in s]))

