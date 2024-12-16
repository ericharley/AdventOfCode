import re

def f(data, offset=0):
  s = ''
  for AX,AY,BX,BY,PX,PY in data:
    PX += offset
    PY += offset
    s += f'''Minimize[{{3*NA + NB, NA*{AX} + NB*{BX} == {PX}, NA*{AY} + NB*{BY} == {PY}}}, {{NA, NB}}, Integers],'''
  s = s[:-1]
  r = f'''Total[Select[{{{s}}}[[All, 1]], # =!= Infinity &]]'''
  return r

lines = open('input.txt').read().strip().split('\n\n')
data = [list(map(int, re.findall(r'\d+', x))) for x in lines]
  
print(f(data,offset=10000000000000))