# with open("test.txt", "r") as file:
with open("input.txt", "r") as file:
  lines = file.read().splitlines()

template = lines[0]
rules = lines[2:]

m = {}
for r in rules:
  (a,b) = r.split(' -> ')
  m[a] = b

input = template
last_ch = input[-1]

def doit(n):
 f = {}
 for i in range(len(input)-1):
   pair = input[i:i+2]
   if pair in f:
     f[pair] += 1
   else:
     f[pair] = 1
 
 for i in range(n):
   out = {}
   for pair in f:
     pair1 = pair[0] + m[pair]
     pair2 = m[pair] + pair[1]
     if pair1 in out:
       out[pair1] += f[pair]
     else:
       out[pair1] = f[pair]
   
     if pair2 in out:
       out[pair2] += f[pair]
     else:
       out[pair2] = f[pair]
   
   f = out

 freq = {}
 for ch in set(''.join(list(f.keys()))):
   freq[ch] = 0
   for k in f:
     if ch in k[0]:
        freq[ch] += f[k]
        
 freq[last_ch] += 1

 max_ch = max(freq, key=freq.get)
 min_ch = min(freq, key=freq.get)

 return (freq[max_ch] - freq[min_ch])

print(doit(10))
print(doit(40))

