#with open("test.txt") as file:
#with open("test2.txt") as file:
#with open("test3.txt") as file:
with open("input.txt") as file:
  lines = file.readlines()

e = {}
for line in lines:
  line = line.rstrip('\n')
  head,tail = line.split('-')

  if head not in e:
    e[head] = {}
  if tail not in e:
    e[tail] = {}
  e[head][tail] = 1
  e[tail][head] = 1


def bfs1(start, end):
  total = 0
  queue = []
  queue.append([start])
  while queue:
    path = queue.pop(0)
    node = path[-1]
    if node == end:
       total += 1
    else:
      for neighbor in list(e[node].keys()):
        if neighbor != start and (neighbor.isupper() or not(neighbor in path)):
          new_path = list(path)
          new_path.append(neighbor)
          queue.append(new_path)

  return total

def crit(path):
  f = [x for x in path if not x.isupper()]
  if len(f) != len(set(f)):
    return False
  else:
    return True

def bfs2(start, end):
  total = 0
  queue = []

  queue.append([start])

  while queue:
    path = queue.pop(0)
    node = path[-1]
    if node == end:
      total += 1
    else:
      for neighbor in list(e[node].keys()):
        if neighbor != start and (neighbor.isupper() or ( not(neighbor in path) or crit(path))):
          new_path = list(path)
          new_path.append(neighbor)
          queue.append(new_path)

  return total

print( bfs1('start', 'end') )
print( bfs2('start', 'end') )
