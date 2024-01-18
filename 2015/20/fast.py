from itertools import product
from itertools import groupby

def get_prime_divisors(n):
    divisors = []
    while n % 2 == 0:
        divisors.append(2)
        n //= 2
    while n % 3 == 0:
        divisors.append(3)
        n //= 3
    i = 5
    while i*i <= n:
        for k in (i, i+2):
            while n % k == 0:
                divisors.append(k)
                n //= k
        i += 6
    if n > 1:
        divisors.append(n)
    return divisors

from functools import reduce
from operator import mul
def prod(val) : 
  return reduce(mul, val)

def get_divisors(i):
  def aggregate(factors):
    def power_up(factors):
      return [[x**i for i in range(a+1)] for x,a in factors]
    for t in product(*power_up(factors)):
      yield prod(t)

  return aggregate([(k,len(list(g))) for k, g in groupby(get_prime_divisors(i))])

# Part 1
n = 29000000
i = 2
while True:
  if n <= 10*sum(get_divisors(i)):
    print(i)
    break
  i += 1

# Part 2
while True:
  if n <= 11*sum([x for x in get_divisors(i) if 50*x >= i]):
    print(i)
    break
  i += 1

