d = {}
s = []

def pwd():
  if len(s) > 1:
    return ('/'.join(s))[1:]
  else:
    return('/')

def cwd():
 return s[-1]

def cd(dir):
 if dir == '..':
   s.pop()
 else:
   s.append(dir)

def calc_size(root):
  size = 0
  for entry in d[root]:
    if type(entry) is tuple:
      size += entry[1]
    else:
      size += calc_size( (root + '/' + entry).replace('//','/',1) )

  return size

getting_files = False

with open("input.txt") as f:
  for line in f:
    line = line.rstrip()

    if getting_files and line[0] != '$':
      x,y = line.split(' ')
      if x == 'dir':
        dir_name = y
        path = pwd()
        if path in d:
          d[path].append( dir_name )
        else:
          d[path] = [ dir_name ]
      else:
        file_size = int(x)
        file_name = y
        path = pwd()
        if path in d:
          d[path].append( (file_name, file_size) )
        else:
          d[path] = [(file_name, file_size) ]

    if line[0:4] == '$ cd':
      getting_files = False
      _,_,y = line.split(' ')
      cd(y)

    if line[0:4] == '$ ls':
      getting_files = True

# Part 1
total_size = 0
for key in d:
 if calc_size(key) <= 100000:
   total_size += calc_size(key)
print(total_size)

# Part 2
sz = {}
for key in d:
  sz[key] = calc_size(key)

total_disk_space = 70000000
free_space_needed = 30000000
current_free_space = total_disk_space - calc_size('/')

the_min = calc_size('/')
the_min_dir = '/'

for key in sz:
  if current_free_space + sz[key] >= free_space_needed:
    if sz[key] < the_min:
      the_min = sz[key]
      the_min_dir = key

print(the_min)


#candidates = [k for k in sz.keys() if current_free_space + sz[k] >= free_space_needed]
#c = min(candidates, key = lambda x : sz[x]) 
#print(sz[c])
