line = open('input.txt').read().strip()

file_id = 0
out = []
l = {}
for j,i in enumerate([int(i) for i in line]):
  if j % 2 == 0:
    out.append((file_id,i))
    l[file_id] = i
    file_id += 1

  else:
    out.append(('.',i))

for file_id in reversed(l):
  file_len = l[file_id]
  p = out.index((file_id,file_len))

  for i,b in enumerate(out[:p]):

    block_id, block_len = b

    if block_id == '.' and block_len >= file_len:
      out[i] = (file_id, file_len)
      out[p] = ('.', file_len)
      out.insert(i+1, ('.', block_len - file_len))
      break

def h(out):
  t,pos = 0,0
  for i,b in out:
    if i != '.':
      t += i*(b*pos + (b-1)*b // 2)
    pos += b
  return t

print(h(out))
