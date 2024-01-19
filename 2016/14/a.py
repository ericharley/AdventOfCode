from functools import cache
import hashlib

salt = "qzyelonm"
#salt = "abc"
@cache
def getvalue(input, counter):
  t = input + str(counter)
  return hashlib.md5(t.encode()).hexdigest()

@cache
def stretched_hash(input, counter):
  hash = getvalue(input, counter)
  for i in range(2016):
    hash = hashlib.md5(hash.encode()).hexdigest()
  return hash

@cache
def triplet(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return s[i]
    return ''

count = 0
i = 0
while count < 64:
  i += 1
  s = getvalue(salt, i)
  if triplet(s) :
    c = triplet(s)
    l = [getvalue(salt, i+j) for j in range(1,1000+1)]
    l = [x for x in l if (5*c) in x]
    if l:
#      print(i, s, c, l)
      count += 1
print(i)

count = 0
i = 0
while count < 64:
  i += 1
  s = stretched_hash(salt, i)
  if triplet(s) :
    c = triplet(s)
    l = [stretched_hash(salt, i+j) for j in range(1,1000+1)]
    l = [x for x in l if (5*c) in x]
    if l:
#      print(i, s, c, l)
      count += 1
print(i)

