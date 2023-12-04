from collections import defaultdict
import re

filename = 'input.txt'
#filename = 'test.txt'

lines = [line.split(': ') for line in open(filename).read().splitlines()]

deck = {}
hand = {}

total = 0
for line in lines:
  k = int(''.join([x for x in line[0] if x.isdigit()]))
  a,b = line[1].split(' | ')
  a = set([int(x) for x in a.split(' ') if x != ''])
  b = set([int(x) for x in b.split(' ') if x != ''])
  n = len(a & b)
  v = round(2**(n-1))
  deck[k] = n
  hand[k] = 1
  total += v
print(total)

def process_card(i):
  n = deck[i]
  for j in range(1,n+1):
    hand[i+j] += 1

N = len(hand)
for i in range(1,N+1):
  for _ in range(hand[i]):
    process_card(i)

score = sum(hand.values())
print(score)
