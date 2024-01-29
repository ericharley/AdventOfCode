t = int(open('input.txt').read())

scores = [3,7]
made_so_far = len(scores)
p1 = 0
p2 = 1

while made_so_far <= t+10:
  n = map(int,str(scores[p1]+scores[p2]))
  scores.extend(n)
  made_so_far = len(scores)
  p1 = (p1 + 1 + scores[p1]) % made_so_far
  p2 = (p2 + 1 + scores[p2]) % made_so_far

print(''.join(map(str,scores[t:(t+10)])))
