from queue import PriorityQueue
from itertools import product 

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [ {} for i in range(num_of_vertices) ]
        self.visited = {}

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight

    def neighbors(self, u):
        return self.edges[u].keys()


def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited[current_vertex] = 1

        for neighbor in graph.neighbors(current_vertex):
           distance = graph.edges[current_vertex][neighbor]
           if neighbor not in graph.visited:
               old_cost = D[neighbor]
               new_cost = D[current_vertex] + distance
               if new_cost < old_cost:
                    D[neighbor] = new_cost
                    pq.put((new_cost, neighbor))
    return D


def risk(a):
  N = len(a)
  g = Graph(N*N)

  def c2v(i,j):
    return N*i + j

  for (i,j) in product(range(N), range(N)):
    for (dx,dy) in product([-1, 0, +1], [-1, 0, +1]):
      if not(dx == 0 and dy == 0) and not(dx != 0 and dy != 0):
        if (0 <= i+dx < N) and (0 <= j+dy < N):
          g.add_edge( c2v(i,j), c2v(i+dx,j+dy), a[i+dx][j+dy] )

  D = dijkstra(g, 0)
  return(D[c2v(N-1,N-1)])


def extend(cave):
    X, Y = len(cave), len(cave[0])
    return [[(cave[x%X][y%Y] + x//X+y//Y - 1)%9+1
        for y in range(5*Y)] for x in range(5*X)]


with open("input.txt", 'r') as f:
    a = [[int(n) for n in list(line.rstrip('\n'))] for line in f]

print( risk(a) )

print( risk(extend(a)) )
