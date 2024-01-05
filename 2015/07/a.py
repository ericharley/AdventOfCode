#NOT dq -> dr
#kg OR kf -> kh
#44430 -> b
#y AND ae -> ag
#lf RSHIFT 2 -> lg
#eo LSHIFT 15 -> es

lines = open('input.txt').read().strip().split('\n')

f = {
'LSHIFT' : lambda x,y : x << y
'RSHIFT' : lambda x,y : x >> y
'AND' : lambda x,y : x & y
'OR' : lambda x,y : x | y
'NOT' : lambda x : ~x
}

for line in lines:

  left,right = line.split(' -> ')

  if 'LSHIFT' in left or 'RSHIFT' in left:
    a, op, b = left.split(' ')
    b = int(b)
    lambda x : f[op](a,b)

  wire[right] = left

  print(line)
