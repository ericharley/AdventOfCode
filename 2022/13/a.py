x = list(map(str.splitlines, open(0).read().strip().split("\n\n")))

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

  return len(x) - len(y)

t = 0
for i, (a,b) in enumerate(x):
  a = eval(a)
  b = eval(b)
  if f(a,b) < 0:
    t += i + 1

print(t)
