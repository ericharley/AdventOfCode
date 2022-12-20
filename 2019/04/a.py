import re

lo,hi = map(int, open('input.txt').readline().rstrip().split('-'))

dd = ['11', '22', '33', '44', '55', '66', '77', '88', '99']

count1 = 0
count2 = 0

for x in range(lo, hi+1,1):

  a = list(str(x))
  b = list(str(x))
  c = list(str(x))

  # Part 1
  if (not any([y in str(x) for y in dd])) or any( [int(aa)>int(bb) for aa,bb in zip(a,b[1:])]  ):
    continue
  count1 += 1

  # Part 2
  a = re.sub(r'(111+|222+|333+|444+|555+|666+|777+|888+|999+)', r'', ''.join(a))
  if not any([y in a for y in dd]):
    continue
  count2 += 1

print(count1)
print(count2)

