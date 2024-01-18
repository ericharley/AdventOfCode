filename = 'input.txt'
val = 150

c = [int(x) for x in open(filename).readlines()]

def f(c,v,k):
 if v == 0 and k == 0:
   return 1

 if (v < 0) or (v == 0 and k != 0) or (v > 0 and c == []):
   return 0

 else:
   first,rest = c[0],c[1:]
   return f(rest, v-first, k-1) + f(rest, v, k)

for i in range(len(c)):
  x = f(c,val,i)
  if x > 0:
    print(x)
    break
