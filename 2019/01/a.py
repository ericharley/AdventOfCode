with open("input.txt","r") as file:
  lines = file.readlines()
v = [int(line.rstrip('\n')) for line in lines]

fuel = sum([(x // 3 - 2) for x in v])
print(fuel)

def total_fuel(mass):
  fuel = mass // 3 - 2
  if fuel <= 0:
    return 0
  else:
    return fuel + total_fuel(fuel)

print(sum(map(total_fuel, v)))
