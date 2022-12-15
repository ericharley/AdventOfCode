filename = 'input.txt'
N = 3

from itertools import zip_longest as izip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

def score(i):
    if badge in set('abcdefghijklmnopqrstuvwxyz'):
       return ord(badge) - ord('a') + 1
    else:
       return ord(badge) - ord('A') + 27

t = 0

with open(filename) as f:
     for lines in grouper(f, N, ''):
         assert len(lines) == N
         # process N lines here
         a = set(lines[0].rstrip())
         b = set(lines[1].rstrip())
         c = set(lines[2].rstrip())
         badge = list(a.intersection(b).intersection(c))[0]
         t += score(badge)

print(t)
