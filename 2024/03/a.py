import re
from operator import mul

line = ''.join(open('input.txt').readlines()).replace('\n','')

# Part 1
print( sum(eval(m) for m in re.findall(r'mul\(\d+,\d+\)', line)) )

# Part 2
line = re.sub(r'don\'t\(\).*?(do\(\)|$)','',line)
print( sum(eval(m) for m in re.findall(r'mul\(\d+,\d+\)', line)) )
