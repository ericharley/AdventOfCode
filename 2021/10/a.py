from statistics import median

closing_match = {
	'{' : '}',
	'(' : ')',
	'<' : '>',
	'[' : ']',
}

cost = {
	')' : 3,
	']' : 57,
	'}' : 1197,
	'>' : 25137,
}

cost2 = {
   '(': 1,
   '[': 2,
   '{': 3,
   '<': 4,
}

total_cost = 0
completion_scores = []

with open("input.txt", "r") as f:
#with open("test.txt", "r") as f:
   lines = f.readlines()

for line in lines:
   line = line.rstrip('\n')

   stack = []
   was_corrupted = False

   for c in line:

     if c in ['(', '[', '<', '{']:
       stack.append(c)

     elif c in [')', ']', '>', '}']:
       top = stack.pop()

       if closing_match[top] != c:
         #print(line, f'Expected {closing_match[top]}, but found {c} instead')
         total_cost += cost[c]
         was_corrupted = True
         break

     else:
        print(f'ERROR Unexpected {c}')
        exit

   if not was_corrupted:
     score = 0

     for c in reversed(stack):
       score *= 5
       score += cost2[c]

     completion_scores.append(score)

print(total_cost)
print(median(completion_scores))
