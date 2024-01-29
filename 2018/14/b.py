t = open('input.txt').read().strip()
g = list(map(int,list(t)))
k = len(g)

scores = [3,7]
p1,p2 = 0,1
pos = 0

while True:
  _p1 = scores[p1]
  _p2 = scores[p2]
  _n = map(int,str(_p1 + _p2))

  scores.extend(_n)
  p1 = (p1 + 1 + _p1) % len(scores)
  p2 = (p2 + 1 + _p2) % len(scores)

  if scores[pos:pos+k] == g:
    print(pos)
    break
  else:
    pos += 1
