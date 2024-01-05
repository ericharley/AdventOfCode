lines = open('input.txt').read().strip().split('\n')
#lines = open('test.txt').read().strip().split('\n')

outputs = {}

q = []
bots = {}
for i in range(300):
  bots[i] = { 'low' : -1, 'high' : -1, 'has':[]  }
  outputs[i] = []

for line in lines:
  if 'value' in line:
    # value 2 goes to bot 2
    value = int(line.split(' ')[1])
    bot = int(line.split(' ')[-1])

    bots[bot]['has'].append(value)

    if len(bots[bot]['has']) == 2:
      q.append(bot)

  if 'gives low to' in line :
    # bot 53 gives low to bot 128 and high to bot 74
    # bot 53 gives low to output 2 and high to output 3
    # a   b                c     d             e      f
     
    a,b,c,d,e,f = line.replace(' gives low to','').replace(' and high to','').split(' ')
    bot = int(b)

    low_type = c
    low = int(d)

    high_type = e
    high = int(f)

    bots[bot]['low'] = (low_type, low)
    bots[bot]['high'] = (high_type, high)

#print(bots)

while q:
  b = q.pop(0)

  lo = min(bots[b]['has'])
  lo_type, lo_to = bots[b]['low']
 
  hi = max(bots[b]['has'])
  hi_type, hi_to = bots[b]['high']

  if lo_type == 'bot':
    bots[lo_to]['has'].append(lo)
    if len(bots[lo_to]['has']) == 2:
      q.append(lo_to)
  else:
    outputs[lo_to].append(lo)

  if hi_type == 'bot':
    bots[hi_to]['has'].append(hi)
    if len(bots[hi_to]['has']) == 2:
      q.append(hi_to)
  else:
    outputs[hi_to].append(hi)

  # print(f'bot {b} gives {lo} to {lo_type} {lo_to}, {hi} to {hi_type} {hi_to}')

  if (lo,hi) == (17,61):
    print(b)
  
#print([f'{key}:{outputs[key]}' for key in outputs if outputs[key] != []])

print(outputs[0][0]*outputs[1][0]*outputs[2][0])

