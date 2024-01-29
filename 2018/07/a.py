import networkx as nx
from collections import defaultdict

lines = open('input.txt').read().strip().splitlines()

G = nx.DiGraph()

pred = defaultdict(set)

for line in lines:
  # Step U must be finished before step A can begin.
  line = line.replace('must be finished before step ','')
  line = line.replace('Step ','')
  line = line.replace(' can begin.','')
  A,B = line.split()
  G.add_edge(A,B)
  pred[B].add(A)

ordering = ''.join(list(nx.lexicographical_topological_sort(G)))

# Part 1
print(ordering)

# Part 2
def job_time(c):
  return (ord(c) - ord('A') + 1) + 60

jobs = list(ordering)
done = set()
started = set()
workers = defaultdict(list)

num_workers = 5

t = -1

while (set(jobs) - done):
  t += 1

  for k in range(num_workers):
    if workers[k]:
      job, timer = workers[k]
      if timer == 1:
        workers[k] = []
        done.add(job)
      else:
        workers[k] = (job,timer-1)

  # for each unstarted, unfinished job that can be started
  for job in jobs:
    if job not in (started|done) and not(pred[job]-done):
      # assign it to the next worker to work if possible
      for k in range(num_workers):
        if not workers[k]:
          workers[k] = (job,job_time(job))
          started.add(job)
          break

print(t)
