_, data = open('input.txt').read().strip().split('\n')
data = data.split(',')

# Remainders
r = []
# Moduli
m = []

for i,v in enumerate(data):
  if v != 'x':
    v = int(v)
    r.append(v-i % v)
    m.append(v)

# Mathematica
#r[0] = 0
#print('ChineseRemainder[', end='')
#print('{' + ','.join(map(str,r)) + '},', end='')
#print('{' + ','.join(map(str,m)) + '}', end='')
#print(']')

def chinese_remainder(r, m):
    from functools import reduce
    from operator import mul

    N = reduce(mul, m)
    sum = 0
    for r_i, m_i in zip(r, m):
        p = N // m_i
        sum += r_i * pow(p, -1, m_i) * p

    return (sum % N)

print(chinese_remainder(r, m))
