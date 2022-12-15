from __future__ import annotations 

def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line

class Directory:
  def __init__(self, name : str, parent : Directory):
    self.name = name
    self.children = []
    self.parent = parent
  def __repr__(self):
#    return f"{self.name} ^ {self.parent}"
    return f"{self.name}"
class File:
  def __init__(self, name : str, size : int):
    self.name = name
    self.size = size
  def __repr__(self):
#    return f"{self.name} ^ {self.parent}"
    return f"{self.name}"

f = open("test.txt")

root = Directory("/", None)

d = {}

cwd = [root]
cur_dir = root

while True:
  line = f.readline().rstrip()
  if not line:
    break
  #print(line)
  if line[0:4] == "$ cd":
    _, _, y = line.split(" ")
    if y == "..":
      cwd.pop()
    else:
      # pull out the directory object from the children of the current working directory
      #cur_dir = next((x for x in cwd[-1].children if x.name == y), None )
      #if cur_dir == None:
      #  print("Shouldn't be here")
        #print(cur_dir)
        #print(cur_dir.children)
      cur_dir = Directory(y, cur_dir)
      cwd.append(cur_dir)

  elif line[0:4] == "$ ls":
    while True:
      new_line = peek_line(f)
      if not new_line or new_line[0] == '$':
        break
      else:
        new_line = f.readline().rstrip()
        x,y = new_line.split()
        size = 0
        name = y
        obj = []
        if x == "dir":
          obj = Directory(name, cur_dir)
        else:
          size = int(x)
          obj = File(name, size)
        #print(f"appending {obj} to dir {cur_dir}")
        cur_dir.children.append(obj)
        
def dir_size(entry) : 
  return 0

def file_size(entry) : 
  return entry.size

def print_dir(root : Directory, indent : int):
#  print(root)
  for entry in root.children:
    if type(entry) == Directory : 
      print('-'*indent,f'{entry}/',f':{dir_size(entry)}')
      print_dir(entry,indent+1)
    elif type(entry) == File :
      print('-'*indent, entry,f':{file_size(entry)}')
    else:
      print('!!')

print("---")
print(root)
print_dir(root, 1)
print("---")

