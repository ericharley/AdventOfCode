bank = list(map(int,open('input.txt').read().strip().split()))

def argmax(b):
  return b.index(max(b))

def doit(bank):
  i = argmax(bank)
  r = bank[i]
  bank[i] = 0
  while r > 0:
    r -= 1
    i = (i + 1) % len(bank)
    bank[i] += 1

def find_cycle(bank,M=10000):
  seen = set()

  for c in range(M):
    if tuple(bank) in seen:
      return c,bank

    seen.add(tuple(bank))
    doit(bank)

  return -1,bank

# Part 1
c,bank = find_cycle(bank)
print(c)

# Part 2
c,bank =find_cycle(bank)
print(c)
