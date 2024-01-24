def match(A,B):
  return (A & 0xFFFF) == (B & 0xFFFF)

def gen(seed,k,M=1):
 A = seed
 while True:
   A = A*k % 2147483647
   if A%M==0:
     yield A

A0 = 618
B0 = 814

# Part 1
gA = gen(A0, 16807)
gB = gen(B0, 48271)

c = 0
for i in range(40*(10**6)):
  if match(next(gA),next(gB)):
    c+=1
print(c)

# Part 2
gA = gen(A0, 16807, 4)
gB = gen(B0, 48271, 8)
c = 0
for i in range(5*10**6):
  a = next(gA)
  b = next(gB)
  if match(a,b):
    c += 1
print(c)


