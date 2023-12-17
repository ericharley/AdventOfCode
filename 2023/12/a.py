data = open("input.txt").read().splitlines()

def convert_to_integers(string):
  # Split the string by '.' and filter out empty strings
  groups = filter(lambda x: x, string.split('.'))
  # Count the number of '#' in each group
  counts = [group.count('#') for group in groups]
  return counts

def g(pattern, numbers) :
  numbers = eval('['+numbers+']')
  return convert_to_integers(pattern) == numbers

def f(pattern, numbers) :
  idx = pattern.find('?')
  if idx != -1 :
    return f(pattern.replace('?','.',1), numbers) + f(pattern.replace('?','#',1), numbers)
  else:
    return g(pattern, numbers)

t = 0
for line in data:
  pattern, numbers = line.split()
  t += f(pattern, numbers)
print(t)
