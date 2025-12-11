from functools import cache

AdjOut = {}

lines = open('input.txt').read().strip().splitlines()
for line in lines:
    frm, tos = line.split(': ')
    AdjOut[frm] = tos.split()

@cache
def count(src, dst):
    if src == dst:
      return 1
    return sum(count(w, dst) for w in AdjOut.get(src,[]))

print( count('you', 'out') )

print( count('svr','dac')*count('dac','fft')*count('fft','out')
     + count('svr','fft')*count('fft','dac')*count('dac','out') )
