import re

line = ''.join(open('input.txt').readlines()).replace('\n','')

def mul(x,y):
  return x*y

# Part 1
print( sum(eval(m) for m in re.findall(r'mul\(\d+,\d+\)', line)) )

# Part 2
line = re.sub(r'don\'t\(\).*?(do\(\)|$)','',line)
print( sum(eval(m) for m in re.findall(r'mul\(\d+,\d+\)', line)) )
