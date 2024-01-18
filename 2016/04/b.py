alpha = 'abcdefghijklmnopqrstuvwxyz'

lines = open('input.txt').read().strip().split('\n')

def is_real(name,checksum):
  l = {c : name.count(c) for c in name if c in alpha}
  l = sorted(l.items(), key=lambda x:(-x[1],x[0]))
  l = [a for a,b in l]
  return (''.join(l[0:5])) == checksum

def decrypt(name,id):
  def dec(c,id):
    if c != '-':
      idx = ((ord(c) - ord('a')) + id) % 26
      return alpha[idx]
    else:
      return ' '

  return ''.join([dec(c,id) for c in name])

t = 0
for s in lines:

  name = '-'.join(s.split('-')[0:-1])

  id = s.split('-')[-1]
  j = id.find('[')
  id = int(id[0:j])

  i = s.find('[')
  checksum = s[i+1:-1]

  if is_real(name, checksum):
    t += id
    if 'northpole' in decrypt(name,id):
      output = id, decrypt(name,id)
  
print(t)
print(output)
