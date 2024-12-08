from operator import mul, add

lines = open('input.txt').read().splitlines()

data = []
for line in lines:
  a, *ns = list(map(int,line.replace(':','').split(' ')))
  data += [(a,ns)]

def f(target, nums):
    results = { nums[0] }

    for n in nums[1:]:
      results = {op(x,n) for x in results for op in ops}

    return target in results

# Part 1
ops = [mul, add]
print( sum([a for a,ns in data if f(a,ns)]) )

# Part 2
ff = lambda a,b : int(f'{a}{b}')
ops = [mul, add, ff]
print( sum([a for a,ns in data if f(a,ns)]) )
