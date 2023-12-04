filename = 'input.txt'
lines = [line for line in open(filename).read().splitlines()]

deck = {}
hand = {}

total = 0
for k, line in enumerate(lines):
  a,b = line.split(': ')[1].split('|')
  a = set( a.split() )
  b = set( b.split() )
  n = len(a & b)

  # Part 1
  total += 2**(n-1) if n > 0 else 0

  # Part 2
  deck[k] = n
  hand[k] = 1

for i in hand:
  for j in range(deck[i]):
    hand[i+j+1] += hand[i]

print(total, sum(hand.values()))
