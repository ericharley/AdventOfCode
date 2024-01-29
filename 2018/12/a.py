from collections import defaultdict

filename = 'input.txt'
num_gen = 20
part_2 = 50*10**9
thresh = 159

# Parse input
initial_state,rules = open(filename).read().strip().split('\n\n')
_,initial_state = initial_state.split(': ')

rules = rules.strip()
rules = rules.splitlines()

# Load rules
m = defaultdict(lambda : '.')
for rule in rules:
  frm,to = rule.split(' => ')
  m[frm] = to

# initialize state
hallway = defaultdict(lambda : '.')
for i,c in enumerate(initial_state):
  hallway[i] = c

def get_hall(h,l,u):
  return ''.join([h[c] for c in range(l,u+1)])

def iterate(h,rule,l,u):
  next_h = defaultdict(lambda : '.')
  for c in range(l,u+1):
    next_h[c] = rule[h[c-2]+h[c-1]+h[c]+h[c+1]+h[c+2]]

  return next_h

last_total = 0
for i in range(1,thresh+3):
  hallway = iterate(hallway,m,l=-10,u=thresh*2)

  # Part 1
  if i == num_gen:
    total = sum([k for k,v in hallway.items() if v == '#'])
    print(total)

  # Stabilized...
  if i >= thresh:
    total = sum([k for k,v in hallway.items() if v == '#'])
    diff = total - last_total
    last_total = total

# Part 2
n = part_2
print( (n-i)*diff+total )

