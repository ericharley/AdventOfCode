x = list(map(eval, open(0).read().split()))

div2 = [[2]]
div6 = [[6]]

x.append(div2)
x.append(div6)

def f(x, y):

  # both ints
  if type(x) == int and type(y) == int:
    return x - y

  # left int -> list
  if type(x) == int:
    return f([x], y)

  # right int -> list
  if type(y) == int:
    return f(x, [y])

  # both lists
  for a,b in zip(x,y):
    # recurse
    v = f(a,b)
    if v :
      return v

  # all elements are equal, return difference in lengths
  return len(x) - len(y)


import functools
cmp_func = lambda x, y: f(x,y)
sorted_x = sorted(x, key=functools.cmp_to_key(cmp_func) )



print( (sorted_x.index(div2)+1) * (sorted_x.index(div6)+1) )
