def decode(v1,v2):
   d = {}
   d[5] = []
   d[6] = []

   for v in v1:
      if len(v) == 2:
        d[1] = set(v)
      elif len(v) == 3:
        d[7] = set(v)
      elif len(v) == 4:
        d[4] = set(v)
      elif len(v) == 7:
        d[8] = set(v)
      elif len(v) == 5:
        d[5].append(set(v))
      elif len(v) == 6:
        d[6].append(set(v))

# For five segment digits:
# if you overlay the digit "1" and it's still five segments, it's a "3"
# len(d[5][k].union(d[1])) => d[5][k] == 5
# {'e', 'f', 'd', 'b', 'c'}
#
# if you overlay the digit "4" and it covers all seven segments, it's a "2"
# len(d[5][k].union(d[4])) => d[5][k] == 2
#
# otherwise it's a 5
# d[5][k] == 5
   fives = d[5]
   for f in fives:
     if len(f.union(d[1])) == 5:
       d[3] = f
     elif len(f.union(d[4])) == 7:
       d[2] = f
     else:
       d[5] = f

# For six segment digits:
# if you overlay the digit "4" and it's still six segments, it's a "9"
# if it shares both segments that also in the digit "1", then it's a "0"
# otherwise it can only be a "6"
   sixes = d[6]
   for f in sixes:
     if len(f.union(d[4])) == 6:
       d[9] = f
     elif len(f.intersection(d[1])) == 2:
       d[0] = f
     else:
       d[6] = f

   m = {}       
   for k in d:
     m[frozenset(d[k])] = k
     
   return m

with open("input.txt", "r") as f:
   lines = f.readlines()

total = 0
for line in lines:
   g = line.rstrip('\n').split(' | ')
   v1 = g[0].split(' ')
   v2 = g[1].split(' ')

   m = decode(v1,v2)

   total += int(''.join(  [str(m[frozenset(v)]) for v in v2]  ) )
   
print(total)