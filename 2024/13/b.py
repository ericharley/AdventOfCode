import re

# NB: Assumes "nice" input
def f(AX,AY,BX,BY,PX,PY,offset=0):

  PX += offset
  PY += offset

  det = (AY*BX - AX*BY)
  det_NA = (BX*PY - BY*PX)
  det_NB = (AY*PX - AX*PY)

  if det_NA % det == 0 and det_NB % det == 0:
    NA = det_NA // det
    NB = det_NB // det

    return 3*NA + NB

  return 0

lines = open('input.txt').read().split('\n\n')
data = [list(map(int, re.findall(r'\d+', x))) for x in lines]

# Part 1
print( sum(f(*x) for x in data) )

# Part 2
print( sum(f(*x, offset=10000000000000) for x in data) )
