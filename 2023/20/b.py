from collections import defaultdict
from math import gcd

lines = open('input.txt').read().strip().split('\n')

nodes = {}
edges = defaultdict(lambda : [])
state = defaultdict(lambda : {})

def parse_input():
 for line in lines:
  frm = line.split(' -> ')[0]
  tos = line.split(' -> ')[1].split(', ')

  typ = frm[0] if frm[0] in '&%' else 'b'
  frm = frm if typ == 'b' else frm[1:]

  nodes[frm] = typ

  for to in tos:
    if to not in nodes:
      nodes[to] = '?'
    edges[frm].append(to)

def push_button(watch):

  q = []
  q.append(('broadcaster',0,'button'))

  while q:
    node, in_value, frm = q.pop(0)
    if frm == watch and node == 'bq' and in_value == 1:
      return 1

    if nodes[node] == 'b':
      out_value = in_value
      for to in edges[node]:
         q.append((to,out_value,node))

    if nodes[node] == '%':
      if in_value == 0:
        state[node] = 'on' if state[node] == 'off' else 'off'
        out_value = 1 if state[node] == 'on' else 0
        for to in edges[node]:
          q.append((to,out_value,node))

    if nodes[node] == '&':
      state[node][frm] = in_value
      if 0 not in list(state[node].values()):
        out_value = 0
      else:
        out_value = 1
      for to in edges[node]:
        q.append((to,out_value,node))

  return 0

def reset_state():
 for node in nodes:
  if nodes[node] == '%':
    state[node] = 'off'

  if nodes[node] == '&':
    for frm in edges:
      if node in edges[frm]:
        state[node][frm] = 0

def find_cycle(node):
 reset_state()
 for i in range(10**5):
  if push_button(node) == 1:
    return(i+1)

def lcm(a, b):
    return abs(a*b) // gcd(a, b)


parse_input()
prev = [key for key in edges if 'rx' in edges[key]].pop() # bq

v = 1
for a in [key for key in edges if prev in edges[key]]:    # tx, vg, kp, gc
  v = lcm(v, find_cycle(a))

print(v)
