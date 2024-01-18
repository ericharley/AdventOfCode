line = open('input.txt').read().strip()

#import re
#matches = re.findall(r'(-?[0-9]+)', line)
#t = 0
#for m in matches:
#  t += int(m)
#print(t)

data = eval(line)

def a(data):
 if type(data) is str:
   return 0

 if type(data) is int:
   return data

 if type(data) is list:
   return sum(map(a, data))

 if type(data) is dict:
   return sum(map(a, data.values()))

def b(data):
 if type(data) is str:
   return 0

 if type(data) is int:
   return data

 if type(data) is list:
   return sum(map(b, data))

 if type(data) is dict:
   if 'red' in data.values():
     return 0
   else:
     return sum(map(b, data.values()))

print(a(data))
print(b(data))
