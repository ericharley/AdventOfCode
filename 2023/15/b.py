ss = open('input.txt').read().strip()
DEBUG = False
  
def HASH(s):
  v = 0
  for ch in s:
    v+= ord(ch)
    v*=17
    v%=256
  return(v)

# Part 1
print(sum([HASH(s) for s in ss.split(',')]))

# Part 2
boxes = [[] for _ in range(256)]
focal_lengths = {}

for s in ss.split(','):
  if '=' in s:
    label, focal_len = s.split('=')
    box_id = HASH(label)

    for i,_ in enumerate(boxes[box_id]):
      l,f = boxes[box_id][i]
      if l == label:
        boxes[box_id][i] = (label,focal_len)
        break
    else:
      boxes[box_id].append((label,focal_len))

  if '-' in s:
    label, focal_len = s.split('-')
    box_id = HASH(label)
    for i,_ in enumerate(boxes[box_id]):
      l,f = boxes[box_id][i]
      if l == label:
        boxes[box_id].pop(i)
        break

  if DEBUG:
    print(f'After "{s}":')
    for i, l in enumerate(boxes):
      if len(boxes[i]) > 0:
        ss = ' '.join([f'[{x[0]} {x[1]}]' for x in boxes[i]])
        print(f'Box {i}: {ss}')


def focusing_power(boxes):
  fp = 0
  for box_idx in range(len(boxes)):
    a = (1 + box_idx)
    for lens_idx in range(len(boxes[box_idx])):
      b = (lens_idx + 1)
      c = int(boxes[box_idx][lens_idx][1])
      fp += a*b*c
      label = boxes[box_idx][lens_idx][0]
#      print(f'{label}: {a} * {b} * {c} = {a*b*c}')
  return fp

print(focusing_power(boxes))
