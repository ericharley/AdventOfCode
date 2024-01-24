def do_dance(ins, s_in):
 s = list(s_in)
 for i in ins:
  if i[0] == 's':
    X = int(i[1:])
    for _ in range(X):
      s = [s[-1]] + s[0:-1]

  if i[0] == 'x':
    A,B = map(int,i[1:].split('/'))
    t = s[A]
    s[A] = s[B]
    s[B] = t

  if i[0] == 'p':
    A,B = i[1],i[3]
    idx_A = s.index(A)
    idx_B = s.index(B)
    t = s[idx_A]
    s[idx_A] = s[idx_B]
    s[idx_B] = t

 return tuple(s)

ins = tuple(open('input.txt').read().strip().split(','))
s = tuple('abcdefghijklmnop')
N = 10**9 

# Part 1
print(''.join(do_dance(ins, s)))

# Part 2
seen = set()
while s not in seen:
  seen.add(s)
  s = do_dance(ins, s)

cycle_len = len(seen)
rem = N % cycle_len
for _ in range(rem):
  s = do_dance(ins, s)
print(''.join(s))
