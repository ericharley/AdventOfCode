import re
import itertools

def explode(num):
#  # idea: go through string and count depth by opening closing [s ]s
  depth = 0
  for i,c in enumerate(num):
    if depth == 4 and c == '[':

      head = num[:i]
      tail = num[i:]

      # Process the right hand side of the pair
      p = r'\[(([0-9]+),([0-9]+))\]'
      m = re.search(p, tail)
      left = m[2]
      right = m[3]
      s = tail.replace(m[0],'',1)
      # find the first number in this string...
      p = '([0-9]+)'
      m = re.search(p, s)
      if m :
        (start, finish) = m.span(1)
        r1 = s[:start] + str(int(s[start:finish]) + int(right)) + s[finish:]
      else:
        r1 = s

      p = '([0-9]+)'
      mlist = [m for m in re.finditer(p,head)]
      if mlist :
        m = mlist[-1]
        (start, finish) = m.span(1)
        r2 = head[:start] + str(int(head[start:finish]) + int(left)) + head[finish:]
      else :
        r2 = head

      return r2 + '0' + r1
      
    if c == '[':
      depth += 1
    if c == ']':
      depth -= 1
  return num



def split(num):
  # Find a number that is greater than 10
  # left := number divided by 2 round down
  # right := number - left
  p = r'([0-9])+'
  for m in re.finditer(p,num):
    if int(m[0]) >= 10:
      (start, finish) = m.span(0)
      left = int(m[0]) // 2
      right = int(m[0]) - left
      new_pair = f'[{left},{right}]'
      return ( num[:start] + new_pair + num[finish:] )

  return num

def reduce(num):
  while True:
    new_num = explode(num)
    if new_num != num:
      num = new_num
      continue
    new_num = split(num)
    if new_num != num:
      num = new_num
      continue
    else:
      break
  return new_num

def add(num_left, num_right):
  return f'[{num_left},{num_right}]'
  

def magnitude(num):
 if isinstance(num[0], int):
   left = 3*num[0]
 else:
   left = 3*magnitude(num[0])
 if isinstance(num[1], int):
   right = 2*num[1]
 else:
   right = 2*magnitude(num[1])
 return left + right

with open("input.txt", "r") as file:
  lines = file.readlines()
  r = lines.pop(0).rstrip('\n')
  for line in lines:
    line = line.rstrip('\n')
    r = reduce(add(r, line))
print(magnitude(eval(r)))

l = []
with open("input.txt", "r") as file:
  lines = file.readlines()
  for i,line in enumerate(lines):
    line = line.rstrip('\n')
    l.append(line)

a = [ magnitude(eval(reduce(add(x,y)))) for x,y in itertools.combinations(l, 2) ]
b = [ magnitude(eval(reduce(add(y,x)))) for x,y in itertools.combinations(l, 2) ]
print( max(a + b) )