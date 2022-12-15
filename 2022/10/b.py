# register
x = 1
xs = []

for line in open(0):
    if line == "noop\n":
      # 1 cycle
      xs.append(x)
    else: # addx v
      v = int(line.split()[1])
      # 2 cycles
      xs.append(x)
      xs.append(x)
      x += v

#signal_strength = clk * x

signal = [(i+1, (i+1)*xs[i]) for i in range(len(xs))]
o = xs
for i in range(0, len(o), 40):
    for j in range(40):
        print(end = "\u2588" if abs(o[i + j] - j) <= 1 else " ")
        # change to "##" and "  " if you have trouble reading the output
    print()

#def drawline(x):
# width = 40
# sprite = list('.'*(width))
# if x == -1:
#   sprite[x+1] = '#'
# elif x == 0:
#   sprite[x] = '#'
#   sprite[x+1] = '#'
# elif x == 39:
#   sprite[x-1] = '#'
#   sprite[x] = '#'
# elif x == 40:
#   sprite[x-1] = '#'
# elif x < -1 or x > 40:
#   # do nothing
#   1
# else:
#   sprite[x-1] = '#'
#   sprite[x]   = '#'
#   sprite[x+1] = '#'
# return( ''.join(sprite) )
