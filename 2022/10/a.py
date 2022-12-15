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

clks = [20, 60, 100, 140, 180, 220]

s = 0
for _,v in [ signal[i-1] for i in clks ] :
  s += v

print(s)
