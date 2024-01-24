import re

line = open('input.txt').read().strip()
line = re.sub(r'!.',r'',line)
part2 = line

# Part 1
line = re.sub(r'<[^>]*>',r'',line)
line = re.sub(r'{,',r'{',line)
line = re.sub(r',}',r'}',line)
line = re.sub(r'{',r'[',line)
line = re.sub(r'}',r']',line)
data = eval(line)

def f(t,d):
  score = d
  for a in t:
    score += (1+f(a,d+1))
  return score

print(1 + f(data,0))
    
# Part 2
part2 = re.sub(r'!.',r'',part2)
print(sum([len(a) for a in re.findall(r'<([^>]*)>', part2)]))
