import hashlib

def t(passcode, path):
  t = passcode + path
  return hashlib.md5(t.encode()).hexdigest()[0:4]

def moves(code):
  output = ''
  if code[0] in 'bcdef':
    output += 'U'
  if code[1] in 'bcdef':
    output += 'D'
  if code[2] in 'bcdef':
    output += 'L'
  if code[3] in 'bcdef':
    output += 'R'

  return output

def isgoal(path):
  x,y = 0,0
  for c in path:
    if c == 'U':
      y -= 1
    if c == 'D':
      y += 1
    if c == 'L':
      x -= 1
    if c == 'R':
      x += 1
  return (x,y)==(3,3)

def isvalid(path):
  r,c = 0,0
  for ch in path:
    if ch == 'U':
      r -= 1
    if ch == 'D':
      r += 1
    if ch == 'L':
      c -= 1
    if ch == 'R':
      c += 1
    if not(0 <= r < 4 and 0 <= c < 4):
      return False
  return True

def doit(passcode):
 visited = {}
 q = []
 path = ''
 
 q.append(path)
 
 while q:
   path = q.pop(0)
   if isgoal(path):
     return(path)
   else:
     for move in moves(t(passcode, path)):
       nxt = path + move
       if isvalid(nxt) and nxt not in visited:
         visited[nxt] = True
         q.append(nxt)

#print(len([x for x in dist if dist[x] <= 50]))

passcode = "pslxynzg"
print(doit(passcode))
