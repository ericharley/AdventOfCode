import numpy as np


def extract_row(a_np,r_idx):
  return a_np[r_idx, :]
  
def extract_col(a_np,c_idx):
  return a_np[:, c_idx]

def convert_np_to_str(r_np):
  str = np.array2string(r_np).replace('.','').replace(' ','').replace('[','').replace(']','')
  str = str.replace('0','.').replace('1','>').replace('2','v')
  return str
  
def convert_str_to_np(r_str):
  r_str = ','.join(list(r_str))
  r_str = r_str.replace('.','0').replace('>','1').replace('v','2')
  return np.fromstring(r_str, sep=',')

def do_step(r_str, ch):
  in_row  = list(r_str)
  out_row = ['.'] * len(in_row)
  for i in range(1,len(in_row)):
    if in_row[i] == '.' and in_row[i-1] == ch:
      out_row[i] = ch
      out_row[i-1] = '.'
    else:
      out_row[i] = in_row[i]
  in_row = out_row
  return(''.join(out_row))

def step_row(r_str):
  return do_step(r_str, '>')

def step_col(r_str):
  return do_step(r_str, 'v')


f = open("test.txt","r")
#f = open("input.txt","r")
lines = f.readlines()
n = len(lines)
for i,line in enumerate(lines):
  lines[i] = lines[i].rstrip('\n')
  lines[i] = lines[i].replace('.', '0').replace('>', '1').replace('v', '2')
  lines[i] = ','.join(list(lines[i]))

a = np.fromstring(lines[0], sep=',')
for i in range(1, len(lines)):
  a = np.vstack([a, np.fromstring(lines[i], sep=',')])

num_rows = np.shape(a)[0]
num_cols = np.shape(a)[1]

print(a)
for step in range(4):
 for r_idx in range(num_rows):
   a[r_idx, :] = convert_str_to_np(step_row(convert_np_to_str(extract_row(a,r_idx))))
 for c_idx in range(num_cols):
   a[c_idx, :] = convert_str_to_np(step_col(convert_np_to_str(extract_col(a,c_idx))))
 print(step)
 print(a)
