lines = open('input5.txt').readlines()

h = set()

def u(x):
  return x[len(x)//2:]

def l(x):
  return x[:len(x)//2]

m = {'F':l,'B':u,'L':l,'R':u}

for s in lines:
 r = list(range(0,128))
 c = list(range(0,8))
 
 for ch in s:
   if ch in 'FB':
     r = m[ch](r)
   elif ch in 'LR':
     c = m[ch](c)

 id = r[0]*8 + c[0]
 h.add(id)

print(max(h))

for id in range(min(h), max(h)):
  if id not in h and (id-1) in h and (id+1) in h:
    print(id)

