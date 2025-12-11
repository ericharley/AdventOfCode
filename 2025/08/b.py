from collections import deque
from math import prod

lines = open('input.txt').read().strip().split()
nodes = [tuple(map(int,line.split(','))) for line in lines]

def connected_components(nodes, edges):
    adj = {u: set() for u in nodes}
    for u, v in edges:
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)

    visited = set()
    components = []

    for start in adj:
        if start in visited:
            continue

        queue = deque([start])
        visited.add(start)
        comp = []

        while queue:
            u = queue.popleft()
            comp.append(u)
            for nbr in adj[u]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)

        components.append(comp)

    return components

def component_sizes(nodes, edges):
  return [len(c) for c in connected_components(nodes, edges)]

def first_one_index(f, n):
    """
    f: function taking index i -> 0 or 1, non-decreasing
    n: length of the implicit array [0..n-1]
    returns index of first 1, or None if all zeros
    """
    lo, hi = 0, n  # search in [lo, hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if f(mid) == 1:
            hi = mid      # mid might be the first 1
        else:
            lo = mid + 1  # first 1 must be to the right

    if lo == n or f(lo) != 1:
        return None
    return lo

dist = lambda a,b : sum([(i-j)**2 for i,j in zip(a,b)])
edges = sorted( [(a,b) for a in nodes for b in nodes if a < b],
                      key=lambda k: dist(*k))

# Part 1
sizes = sorted(component_sizes(nodes, edges[:1000]), reverse=True)
print(prod(sizes[:3]))


# Part 2
f = lambda k : ( len(connected_components(nodes,edges[:k+1])) == 1 )
a,b = edges[ first_one_index(f,len(edges)) ]
print( a[0]*b[0] )
