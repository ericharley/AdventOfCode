lines = open('input.txt').read().strip().split('\n')

# Remainders
r = []
# Moduli
m = []

for line in lines:
  f = line.split()
  disc_num = int(f[1][1:])
  disc_num_pos = int(f[3])
  disc_pos_t0 = int(f[-1][0:-1])

  r.append(-(disc_num+disc_pos_t0))
  m.append(disc_num_pos)

# Mathematica
# ChineseRemainder[{-16, -4, -7, -6, -7, -6, -7}, {17, 3, 19, 13, 7, 5, 11}]
# ChineseRemainder[{-16, -4, -7, -6, -7, -6}, {17, 3, 19, 13, 7, 5}]
#
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

# Part 1
# 
print(chinese_remainder(r, m))

disc_num = len(lines)+1
disc_num_pos = 11
disc_pos_t0 = 0

# Part 2
# 
r.append(-(disc_num+disc_pos_t0))
m.append(disc_num_pos)
print(chinese_remainder(r, m))

