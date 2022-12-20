import collections

f = open("input.txt")
lines = f.readlines()

p = {}
d = {}

for line in lines:
 a,b = line.rstrip().split(')')
 p[b] = a

 if a not in d:
   d[a] = []
 d[a].append(b)

 if b not in d:
   d[b] = []
 d[b].append(a)


# Part 1
def n(obj):
  if obj == 'COM':
    return 0
  return n(p[obj]) + 1  

print( sum([n(obj) for obj in p]) )

# Part 2
def bfs(graph, start, goal):
    visited, queue = set(), collections.deque([(0,start)])
    visited.add(start)

    while queue:
        cost,vertex = queue.popleft()
        if vertex == goal:
          return cost

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((cost+1,neighbour))


start = 'YOU'
goal = 'SAN'
print(bfs(d, start, goal) - 2)
