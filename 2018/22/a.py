import networkx as nx
from functools import cache

start = (0,0)
depth = 10689
target = (11,722)

@cache
def g(x,y):
  if (x,y) in [start,target]:
    return 0
  elif (x == 0) or (y == 0):
    return (x * 16807) + (y * 48271) 
  else:
    return e(x-1,y) * e(x,y-1)

def e(x,y):
  return (g(x,y) + depth) % 20183

def t(x,y):
  return ['rocky','wet','narrow'][e(x,y) % 3]

# Part 1
total = sum([(e(x,y)%3) for y in range(target[1]+1) for x in range(target[0]+1)])
print(total)

# Part 2
start_state = (0,0,(0,1))
end_state = (target[0],target[1],(0,1))

#(rope, torch)
states = {
 'rocky' : {(0,1),(1,0)},
 'wet'   : {(0,0),(1,0)},
 'narrow': {(0,0),(0,1)}
}

G = nx.Graph()

for y in range(target[1]+15):
  for x in range(target[0]+15):
    type_frm = t(x,y)

    # change gear
    for state_frm in states[type_frm]:
      for state_to in states[type_frm]:
        if state_frm != state_to:
          G.add_edge((x,y,state_frm),(x,y,state_to), weight=7)

    # move
    for _x,_y in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]:
      if 0 <= _x and 0 <= _y:
        type_to = t(_x,_y)
        for state in (states[type_frm] & states[type_to]):
          G.add_edge((x,y,state),(_x,_y,state),weight=1)

length = nx.shortest_path_length(G, start_state, target=end_state, weight='weight')
print(length)
