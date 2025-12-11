def split_into_k_parts(s: str, k: int):
    n = len(s)
    part_len = n // k
    return [s[i:i + part_len] for i in range(0, n, part_len)]

def all_equal(l):
    return all(x == l[0] for x in l)

def is_invalid2(s,m=10):
  n = len(s)
  for k in range(2,m):
    if n % k == 0:
      if all_equal(split_into_k_parts(s,k)):
        return True

  return False

part1,part2 = 0,0
data = open('input.txt').readline().strip().split(',')
ranges = [map(int, x.split('-')) for x in data]
for b,c in ranges:
  for i in range(b,c+1):
    s = str(i)
    if is_invalid2(s,3):
      part1 += i
    if is_invalid2(s,8):
      part2 += i

print(part1)
print(part2)