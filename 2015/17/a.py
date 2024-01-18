lines = open('input.txt').read().strip().split('\n')
c = [int(x) for x in lines]

def f(c,v):
 if v < 0 or v > 0 and c == []:
   return 0

 elif v == 0:
   return 1

 else:
   first,rest = c[0],c[1:]
   return f(rest, v - first) + f(rest, v)

print(f(c,150))
