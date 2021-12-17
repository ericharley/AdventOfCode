# with open("test.txt", "r") as file:
with open("input.txt", "r") as file:
  lines = file.read().splitlines()

template = lines[0]
rules = lines[2:]

m = {}
for r in rules:
  (a,b) = r.split(' -> ')
  m[a] = b

input = template

# print('Template:', input)
for n in range(10):
  # print('.', end='',flush=True)
  print(n)
  output = ''

  for i in range(len(input)-1):
   pair = input[i:i+2]
   output += pair[0] + m[pair]

  output += template[-1]
  # print('After step ',n+1,':',output)
  input = output
print()

freq = { ch : output.count(ch) for ch in set(output) }
# print(str(freq))
max_ch = max(freq, key=freq.get)
min_ch = min(freq, key=freq.get)

print(freq[max_ch] - freq[min_ch])
