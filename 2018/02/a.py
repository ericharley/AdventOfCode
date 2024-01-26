ids = open('input.txt').read().strip().split('\n')

def two(id):
  return (2 in [id.count(ch) for ch in id])

def three(id):
  return (3 in [id.count(ch) for ch in id])

# Part 1
print(sum([two(id) for id in ids]) * sum([three(id) for id in ids]))

# Part 2
def common(a,b):
  return ''.join([a[i] for i in range(len(a)) if a[i] == b[i]])

def match_off_by_one(a,b):
  return len(common(a,b)) == len(a) - 1

for a in ids:
  for b in ids:
    if a<b and match_off_by_one(a,b) :
      print(common(a,b))
