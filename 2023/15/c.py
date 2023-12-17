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
    focal_len = int(focal_len)
    box_id = HASH(label)

    if label not in boxes[box_id]:
      boxes[box_id].append(label)

    focal_lengths[label] = focal_len

  if '-' in s:
    label, _ = s.split('-')
    box_id = HASH(label)

    if label in boxes[box_id]:
        boxes[box_id].remove(label)

  if DEBUG:
    print(f'After "{s}":')
    for i, l in enumerate(boxes):
      if len(boxes[i]) > 0:
        ss = ' '.join([f'[{x} {focal_lengths[x]}]' for x in boxes[i]])
        print(f'Box {i}: {ss}')
    print()


def focusing_power(boxes):
  fp = 0

  for box_idx, box in enumerate(boxes):
    for lens_idx, label in enumerate(box):
       fp += (box_idx+1)*(lens_idx + 1)*focal_lengths[label]
       if DEBUG:
         a = (box_idx+1)
         b = (lens_idx + 1)
         c = focal_lengths[label]
         print(f'{label}: {a} * {b} * {c} = {a*b*c}')

  return fp

print(focusing_power(boxes))
