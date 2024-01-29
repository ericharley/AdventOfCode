data = list(map(int,open('input.txt').read().strip().split()))

header_len = 2

def parse_tree(data):

  num_children, num_metadata = data[0:header_len]

  if num_children == 0:
    metadata = data[header_len:header_len+num_metadata]
    return [None, metadata], (header_len+num_metadata)

  else:
    pos = header_len
    output = []
    for _ in range(num_children):
      subtree, subtokens = parse_tree(data[pos:])
      pos += subtokens
      output.append(subtree)
    metadata_entries = data[pos:pos+num_metadata]
    return [output, metadata_entries], pos+num_metadata

tree, tokens = parse_tree(data)

# Part 1
def walk(tree):
  subtrees, metadata = tree

  if not subtrees:
    return sum(metadata)

  s = 0
  for subtree in subtrees:
     s += walk(subtree)
  return s + sum(metadata)

print(walk(tree))

# Part 2
def walk(tree):
  subtrees, metadata = tree

  if not subtrees:
    return sum(metadata)

  v = {(i+1):walk(subtree) for i,subtree in enumerate(subtrees)}
  s = 0
  for idx in metadata:
    if idx in v:
      s += v[idx]
  return s

#tree, tokens = parse_tree([0, 3, 10, 11, 12])
print(walk(tree))

