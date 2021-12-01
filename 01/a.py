with open('input.txt') as f:
    lines = f.readlines()

last = -1
increases = 0
decreases = 0

for line in lines:

    num = int(line)

    if last == -1:
      print(f'{num} (N/A - no previous measurement)')
    elif last < num:
      print(f'{num} (increased)')
      increases += 1
    elif last > num:
      print(f'{num} (decreased)')
      decreases += 1
    else:
      print(f'{num} (no change)')

    last = num

print(f'there are {increases} measurements that are larger than the previous measurement')
