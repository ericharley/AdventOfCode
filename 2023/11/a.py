import itertools

grid = open('input.txt').read().splitlines()

empty_rows = [r for r, row in enumerate(grid) if all(ch == "." for ch in row)]
empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch == "." for ch in col)]

points = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"]

def exp_dist(a,b,rows,cols,scale):
   def dist(a,b):
     return abs(a[0]-b[0])+abs(a[1]-b[1])
   extra_rows = scale - 1
   extra_cols = scale - 1
   min_r = min(a[0], b[0])
   max_r = max(a[0], b[0])
   min_c = min(a[1], b[1])
   max_c = max(a[1], b[1])
   return dist(a,b) + sum([extra_rows for r in rows if min_r<=r<=max_r]) + sum([extra_cols for c in cols if min_c<=c<=max_c])

total_2 = 0
total_1m = 0
for a,b in itertools.combinations(list(points),2):
  total_2 += exp_dist(a,b,empty_rows, empty_cols, 2)
  total_1m += exp_dist(a,b,empty_rows, empty_cols, 10**6)

print(total_2, total_1m)
