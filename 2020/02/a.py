from collections import Counter
lines = open('input2.txt').readlines()
t = 0
for line in lines:
  lo, hi, ch, passwd = line.replace('-',' ').replace(':','').split()
  c = Counter(passwd)
  if int(lo) <= c[ch] <= int(hi):
    t += 1

print(t)


t = 0
for line in lines:
  lo, hi, ch, passwd = line.replace('-',' ').replace(':','').split()
  lo, hi = int(lo),int(hi)
  try:
    if (passwd[lo-1]==ch) ^ (passwd[hi-1]==ch) :
      t+=1
  except:
    pass
print(t)
