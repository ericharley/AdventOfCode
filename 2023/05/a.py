seeds, *blocks = open('input.txt').read().split("\n\n")
seeds = list(map(int, seeds.split(":")[1].split()))

# we're going to map each seed through this block
for block in blocks:
   ranges = []
   for line in block.splitlines()[1:]:
     ranges.append( list(map(int, line.split())) )

   new = []

   for x in seeds:
      for a,b,c in ranges:

        if b <= x < b + c:
          new.append(x + a - b)
          break

      else:
        new.append(x)

   seeds = new

print(min(seeds))

