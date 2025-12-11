intervals,ids = open('input.txt').read().strip().split('\n\n')
intervals = [
    tuple(map(int, line.split('-')))
    for line in intervals.splitlines() if line.strip()
]
ids = [int(x) for x in ids.split()]

# Part 1
print( sum([ any(l <= id <= r for (l, r) in intervals) for id in ids ]) )

# Part 2
def union_size(intervals):
    intervals = sorted(intervals)

    total = 0
    cur_start, cur_end = intervals[0]

    for s, e in intervals[1:]:
        if s <= cur_end + 1:
            cur_end = max(cur_end, e)
        else:
            total += cur_end - cur_start + 1
            cur_start, cur_end = s, e

    total += cur_end - cur_start + 1
    return total

print( union_size(intervals) )
