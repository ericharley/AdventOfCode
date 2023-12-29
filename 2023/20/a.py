from collections import defaultdict

lines = open('input.txt').read().strip().split('\n')

nodes = {}
edges = defaultdict(lambda : [])

state = defaultdict(lambda : {})

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

for node in nodes:
  if nodes[node] == '%':
    state[node] = 'off'

  if nodes[node] == '&':
    for frm in edges:
      if node in edges[frm]:
        state[node][frm] = 0

def push_button(DEBUG):

  count = [0,0]

  q = []
  q.append(('broadcaster',0,'button'))

  while q:
  #  print(q)

    node, in_value, frm = q.pop(0)
    count[in_value] += 1

    if DEBUG:
      print(f'{frm} -{"high" if in_value else "low"}-> {node}')

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

  return count

flip_flops = [frm for frm in nodes if nodes[frm] == '%']

DEBUG = 0

total_count = [0,0]
for i in range(1000):
  count = push_button(0)
  total_count[0] += count[0]
  total_count[1] += count[1]

print(total_count[0]*total_count[1])
