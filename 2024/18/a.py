import networkx as nx

filename = 'input.txt'
n = 1024
w = 71

#filename = 'test.txt'
#n = 12
#w = 7

start = 0,0
end = w-1,w-1

lines = open(filename).read().strip().split('\n')
bad_bytes = [tuple(map(int,line.split(','))) for line in lines]

G = nx.grid_2d_graph(w,w)

G.remove_nodes_from(bad_bytes[:n])

# Part 1
path = nx.shortest_path(G, start, end)
print( len(path) - 1 )

# Part 2
for a,b in bad_bytes[n:]:
  G.remove_node((a,b))
  try:
    if (a,b) in path:
      path = nx.shortest_path(G, start, end)
  except:
    print(f'{a},{b}')
    break
