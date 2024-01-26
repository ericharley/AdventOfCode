data = open('input.txt').read().strip()

def react(data):
  prev_len = -1
  while prev_len != len(data):
    prev_len = len(data)
    for A in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      a = A.lower()
      data = data.replace(A+a,'').replace(a+A,'')
  return data

# Part 1
data = react(data)
n = len(data)
print(n)

# Part 2
min_n = len(data)
for _A in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
  _a = _A.lower()
  _data = data.replace(_A,'').replace(_a,'')
  min_n = min(min_n, len(react(_data)))
print(min_n)
