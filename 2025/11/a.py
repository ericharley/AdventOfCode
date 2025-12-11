from collections import defaultdict
from math import prod

A = defaultdict(int)
AdjInc = defaultdict(set)
nodes = set()

lines = open('input.txt').read().strip().splitlines()
for line in lines:
  frm, tos = line.split(': ')
  tos = tos.split()

  for to in tos:
    AdjInc[to].add(frm)
    A[frm,to] = 1
    nodes.add(frm)
    nodes.add(to)

count = defaultdict(int)
Ak = A

while True:
  count['you','out'] += Ak['you','out']
  
  count['svr','fft'] += Ak['svr','fft']
  count['fft','dac'] += Ak['fft','dac']
  count['dac','out'] += Ak['dac','out']

  count['svr','dac'] += Ak['svr','dac']
  count['dac','fft'] += Ak['dac','fft']
  count['fft','out'] += Ak['fft','out']

  nonzero = False
  Akp1 = defaultdict(int)

  for i in nodes:
   for j in nodes:
    for k in AdjInc[j]:
      Akp1[i,j] += Ak[i,k]*A[k,j]
      nonzero = nonzero or (Ak[i,k]*A[k,j] > 0)

  if not nonzero:
    break

  Ak = Akp1

print( count['you', 'out'] )

print( count['svr','dac']*count['dac','fft']*count['fft','out']
     + count['svr','fft']*count['fft','dac']*count['dac','out'] )