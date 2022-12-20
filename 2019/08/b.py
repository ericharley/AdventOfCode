f = open("input.txt")
data = [int(x) for x in f.readline().rstrip()];

width = 25
height = 6
area = width*height

#Part 1
l = [ len([x for x in data[start:(start+area)] if x == 0]) for start in range(0, 15000, 150) ]
val, idx = min((val, idx) for (idx, val) in enumerate(l))
start = area*idx
n1 = len([x for x in data[start:(start+area)] if x == 1])
n2 = len([x for x in data[start:(start+area)] if x == 2])
print(n1 * n2)

# Part 2
layers = [data[start:(start+area)] for start in range(0, 15000, 150) ]

final_layer = [0]*area
for x in range(len(layers[0])):
 for i in range(len(layers)):
  if layers[i][x] == 1 or layers[i][x] == 0:
    final_layer[x] = layers[i][x]
    break

def print_image(matrix):
 for line in matrix:
  output = ''.join([{1:'█',0:' '}[x] for x in line])
  print(output)

def to_matrix(l, n):
  return [l[i:i+n] for i in range(0, len(l), n)]

print_image(to_matrix(final_layer,width))

