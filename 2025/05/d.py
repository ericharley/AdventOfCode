from bisect import bisect_left

class Diet:
    """Discrete Interval Encoding structure for inclusive integer intervals."""
    def __init__(self):
        # Invariant: intervals are disjoint, sorted, and non-adjacent:
        # e.g. [(3, 5), (10, 14), (16, 20)]
        self.intervals = []
        self.starts = []   # parallel list of starts for bisect

    def add(self, a, b):
        """Add inclusive interval [a, b] to the DIET, merging overlaps."""
        if a > b:
            a, b = b, a

        intervals = self.intervals
        starts = self.starts

        if not intervals:
            intervals.append((a, b))
            starts.append(a)
            return

        # Find index of first interval whose start >= a
        i = bisect_left(starts, a)

        # Maybe merge with previous interval
        if i > 0 and intervals[i - 1][1] + 1 >= a:
            i -= 1
            a = min(a, intervals[i][0])
            b = max(b, intervals[i][1])

        # Merge with subsequent intervals that overlap or touch
        j = i
        while j < len(intervals) and intervals[j][0] <= b + 1:
            a = min(a, intervals[j][0])
            b = max(b, intervals[j][1])
            j += 1

        # Replace intervals[i:j] with the merged [a, b]
        intervals[i:j] = [(a, b)]
        starts[i:j] = [a]

    @property
    def size(self):
        """Total size of the union (for inclusive intervals)."""
        return sum(e - s + 1 for s, e in self.intervals)

    def contains(self, x: int) -> bool:
        """Return True if x is in any stored interval (O(log n))."""
        intervals = self.intervals
        starts = self.starts

        lo, hi = 0, len(intervals) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            s, e = intervals[mid]
            if x < s:
                hi = mid - 1
            elif x > e:
                lo = mid + 1
            else:
                return True
        return False

    def __contains__(self, x: int) -> bool:
        return self.contains(x)

    def __repr__(self):
        return f"Diet({self.intervals})"

l = open('input.txt').read().strip().split('\n\n')
ranges = l[0].split('\n')
ids = list(map(int,l[1].split('\n')))

d = Diet()
for r in ranges:
  x,y = list(map(int, r.split('-'))) 
  d.add(x,y)

print( sum([id in d for id in ids]) )

print( d.size )
