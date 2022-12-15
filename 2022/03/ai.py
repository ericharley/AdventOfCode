total = 0
with open('input.txt') as f:
    lines = f.readlines()

for i in range(0, len(lines), 3):
#    print(lines[i].strip())
#    print(lines[i+1].strip())
#    print(lines[i+2].strip())
#    print()

    common = set(lines[i].strip()) & set(lines[i+1].strip()) & set(lines[i+2].strip())
#    print(common)
#    print()

    values = []
    for c in common:
        if c.islower():
            values.append(ord(c) - 96)
        else:
            values.append(ord(c) - 38)

#    print(values)
#    print()
    total += sum(values)
#    print(sum(values))
#    print()

print(total)
