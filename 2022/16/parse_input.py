for line in open(0):
  line = line.rstrip()
  # 'IY'
  valve = line.split(' ')[1]
  # 0
  flow = int(line.split(' ')[4][5:][:-1])
  # ['VC', 'NT']
  l = ''.join(line.split(' ')[9:]).split(',')

  print(f" f['{valve}'] = {flow}")
  print(f" n['{valve}'] = {l}")
