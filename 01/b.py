with open('input.txt') as f:
    lines = f.readlines()

last = -1
increases = 0
decreases = 0

window_size = 3

for i in range(len(lines) - window_size + 1):
    num = sum([int(x) for x in lines[i: i + window_size]])

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
