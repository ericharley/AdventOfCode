d = {}
f = open("input.txt")

for line in f.readlines():
  monke, r = line.rstrip().split(': ')
  if len(r) == 11:
    left = r[0:4]
    op = r[5:6]
    right= r[7:]
    d[monke] = (op,left,right)
  elif len(r) == 1 or len(r) == 2 or len(r) == 4:
    right = int(r)
    d[monke] = right

def f(root):
   if type(d[root]) == int :
     return d[root]
   else :
     op = d[root][0]
     left = d[root][1]
     right = d[root][2]
     if op == '+':
       return f(left) + f(right)
     elif op == '-':
       return f(left) - f(right)
     elif op == '*':
       return f(left) * f(right)
     elif op == '/':
       return f(left) // f(right)

# Part 1
print(f('root'))


# Part 2
# fix up root so that left and right sides being equal means node
# evaluates to 0
_,left,right = d['root']
d['root'] = ('-',left,right)

# get value of root for given value of humn
def f2(x):
   old_humn = d['humn']
   d['humn'] = x
   val = f('root')
   d['humn'] = old_humn
   return(val)

# now find value for humn that makes f(root) == 0
def sign(x):
  if x > 0:
    return +1
  elif x < 0:
    return -1
  else:
    return 0

# Bisection root search
# found these by hand for the input given
a = 10**12  # f2(a) == -22291452152774
b = 10**13  # f2(b) == 10689147494494

while True:
  c = (a + b)//2
  sa = sign(f2(a))
  sb = sign(f2(b))
  sc = sign(f2(c))
  if sc == 0:
    print(c)
    break
  if sa != sc:
    a = a
    b = c
  else:
    a = c
    b = b
