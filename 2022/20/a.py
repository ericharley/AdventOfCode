from collections import deque

f = open("input.txt")
numbers = [int(line.rstrip()) for line in f.readlines()]


def doit(numbers, key, times):

  pairs = [ ( index, number*key ) for index, number in enumerate( numbers ) ]
  z = numbers.index(0)
  N = len(numbers)

  d = deque(pairs)

  for _ in range(times):
   for idx,val in pairs:
    # Find the thing we're moving
    i = d.index((idx,val))
    d.remove((idx,val))
    d.rotate(-val)
    d.insert(i,(idx,val))
  
  i = d.index((z,0))
  s = d[(i + 1000) % N][1] + d[(i + 2000) % N][1] + d[(i + 3000) % N][1] 

  return(s)


# part 1
#
print(doit(numbers, 1, 1))


# part 2
#
print(doit(numbers, 811589153, 10))
