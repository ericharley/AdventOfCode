lines = open('input.txt').readlines()
reports = [list(map(int,line.split())) for line in lines]

def is_safe(report):
  diffs = [y-x for x,y in zip(report,report[1:])]
  return all([1 <= x <= 3 for x in diffs]) or all([-3 <= x <= -1 for x in diffs])

def drop_one(report):
  return [report[:idx] + report[idx+1:] for idx in range(len(report))]

# part 1
print( sum([is_safe(a) for a in reports]) )

# part 2
print( sum([any(is_safe(b) for b in drop_one(a)) for a in reports]) )
