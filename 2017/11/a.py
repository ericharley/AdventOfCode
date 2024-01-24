dirs = open('input.txt').read().strip().split(',')

q,r = 0,0

m = {
 'n'  : (0,-1),
 's'  : (0,+1),
 'ne' : (+1,-1),
 'nw' : (-1,0),
 'se' : (+1,0),
 'sw' : (-1,+1),
}

def axial_distance(aq,ar, bq,br):
    return (abs(aq - bq) 
          + abs(aq + ar - bq - br)
          + abs(ar - br)) // 2

max_so_far = 0
for d in dirs:
  q,r = q+m[d][0], r+m[d][1]
  max_so_far = max(axial_distance(0,0, q,r), max_so_far)

print(axial_distance(0,0, q,r))
print(max_so_far)
