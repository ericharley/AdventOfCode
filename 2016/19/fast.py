#resets at powers of 3
#
#counts by 1 until
#
#then counts by 2 until ...
#
#[3**3 + 1,(3**3)*2,3**4]
#reset to 1 at first number
#count by 2 after second number until third number


import math

n = 3018458

k = math.floor(math.log(n,3))
print(k)
#if it's a power of three...
#if 3**k == n:

o = 0
for i in range((3**k) + 1, (3**k)*2):
  o += 1
  if i == n:
    print(o)
    exit()
for i in range((3**k)*2, (3**(k+1))+1):
  o += 2
  if i == n:
    print(o)
    exit()
print(o)
