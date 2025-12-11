from functools import lru_cache

@lru_cache
def J2(s,k):
  if k == 0:
    return int(max(set(s)))
  if len(s) == k:
    return int(s)
  if len(s) > k:
    a = int(s[0])
    return max( (10**k)*a + J2(s[1:],k-1), J2(s[1:],k))

lines = open('input.txt').read().strip().split('\n')

part1,part2 = 0,0
for line in lines:
  part1 += J2(line,1)
  part2 += J2(line,11)

print(part1)
print(part2)