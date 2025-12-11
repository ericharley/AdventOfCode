from itertools import accumulate

lines = open('input.txt').read().strip().replace('R','+').replace('L','-').split()
steps = list(map(int, lines))

# Part 1
print( sum( [(x % 100 == 0) for x in accumulate([50]+steps)]) )

start=50
mod=100
pos = start
hits = 0

for dist in steps:
	step = 1 if dist > 0 else -1
	dist = abs(dist)

	# distance (in clicks) from current position to the next time we hit 0
	if step == 1:              # moving right
		# pos + k ≡ 0 (mod 100) ⇒ k ≡ -pos ≡ (100 - pos) mod 100
		k0 = (mod - pos) if pos > 0 else mod
	else:                      # moving left
		# pos - k ≡ 0 (mod 100) ⇒ k ≡ pos (mod 100)
		k0 = pos if pos > 0 else mod

	if k0 <= dist:
		hits += 1 + (dist - k0) // mod

	# update final position after this rotation
	pos = (pos + step * dist) % mod

print(hits)