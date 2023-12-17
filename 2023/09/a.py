lines = open('input.txt').readlines()
data = []
for line in lines:
  line = list(map(int, line.split()))
  data.append(line)

def diff(x):
  def diff_2(x,y):
    d = []
    for a,b in list(zip(x, y)):
      d.append(a - b)
    return d

  return diff_2(x[1:],x[:-1])

def is_zero(x):
  return all([0 == y for y in x])

def extrapolate(seq):
  if is_zero(seq):
    return seq + [0]
  else:
    a = extrapolate( diff(seq) )
    b = seq[-1] + a[-1]
    return seq + [b]

def extrapolate_back(seq):
  if is_zero(seq):
    return [0] + seq
  else:
    a = extrapolate_back( diff(seq) )
    b = seq[0] - a[0]
    return [b] + seq

def extrapolate_back(seq):
  return extrapolate(seq[::-1])[::-1]

# Part 1
t = 0
for seq in data:
  e_seq = extrapolate(seq)
  t += e_seq[-1]
print(t)

# Part 2
t = 0
for seq in data:
  e_seq = extrapolate_back(seq)
  t += e_seq[0]
print(t)

