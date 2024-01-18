import string

lines = open('input.txt').read().strip().split('\n')

def is_real(name,checksum):
  l = {c : name.count(c) for c in name if c in string.ascii_letters}
  l = sorted(l.items(), key=lambda x:(-x[1],x[0]))
  l = [a for a,b in l]
  return (''.join(l[0:5])) == checksum

t = 0
for s in lines:

  name = '-'.join(s.split('-')[0:-1])

  id = s.split('-')[-1]
  j = id.find('[')
  id = int(id[0:j])

  i = s.find('[')
  checksum = s[i+1:-1]

  t += id if is_real(name, checksum) else 0
  
print(t)
