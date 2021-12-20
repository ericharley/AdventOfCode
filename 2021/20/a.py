from itertools import product

img = {}
#with open("test.txt","r") as file:
with open("input.txt","r") as file:
  table = file.readline().rstrip('\n')
  file.readline()
  lines = file.readlines()
  r = 0
  c = 0
  for line in lines:
    line = line.rstrip('\n')
    for c in range(len(line)):
      if line[c] == '#':
        img[(r,c)] = '1'
    r += 1
    #print(line,'E')

# print(img)


def neighbors(inp, d):
  (x,y) = inp
  o = ''
  for dx,dy in product([-1,0,1],[-1,0,1]):
    p = (x+dx, y+dy)
    o += img.get(p, d)
  return o

# print( neighbors((2,2)) )

def lookup(in_bin_str, table):
  v = int(in_bin_str,2)
  if table[v] == '#':
    return '1'
  else:
    return '0'

def evolve(img_in, table, d):
  img_out = {}
  for p in img_in.keys():
    (x,y) = p
    for dx,dy in product([-1,0,1],[-1,0,1]):
      pp = (x+dx, y+dy)
      str = neighbors(pp, d)
      out_value = lookup(str, table)
      if out_value == '1':
        img_out[pp] = out_value
      elif out_value == '0':
        img_out[pp] = out_value
        #del img_out[pp]
      else:
        print('ERROR')
        exit()

  return img_out

orig_img = img.copy()

img = orig_img.copy()
for i in range(2):
 img = evolve(img, table, ('0' if i % 2 == 0 else '1'))
print(len([x for x in img.keys() if img[x] == '1']))

img = orig_img.copy()
for i in range(50):
 img = evolve(img, table, ('0' if i % 2 == 0 else '1'))
print(len([x for x in img.keys() if img[x] == '1']))
