import math
n = 29000000

def get_divisors(n):
  for i in range(1, math.ceil(math.sqrt(n))):
    if n % i == 0:
      yield i
      yield n//i

i = 2
while True:
  if n <= 10*sum(x for x in get_divisors(i)):
    print(i)
    break
  i += 1

i = 665280

while True:
  t = 11*sum([x for x in get_divisors(i) if 50*x >= i])
  if t >= n:
    print(i)
    break
  i += 1

