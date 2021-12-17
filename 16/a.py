from functools import reduce
from operator import mul

# Type 4 : Literal Value
def decode_value(input):
  output = ''
  j = 0
  input = list(input)
  for chunk in [input[i:i+5] for i in range(0,len(input),5)]:
    output += ''.join(chunk[1:])
    j += 1
    if chunk[0] == '0':
      break
  return (int(output, 2), 5*j)

# input: binary string
# output: (packet info, length bits consumed of input)
def parse_packet(p):
  parsed_packet = []
  length_bits_consumed = 0

  V = int(p[0:3], 2) # get_version(p) # 3
  T = int(p[3:6], 2) # get_type(p)    # 3
  p = p[6:]
  length_bits_consumed += 6
  
  if T == 4:
    (val,l) = decode_value(p)
    parsed_packet = [V,T,val]
    length_bits_consumed += l
    return (parsed_packet, length_bits_consumed)
    
  elif T != 4:
    I = int(p[0],2) # 1
    p = p[1:]
    length_bits_consumed += 1
    parsed_subpackets = []
    subpacket_total_length_bits_consumed = 0
    
    if I == 0:
      sub_packet_length = int(p[0:15], 2) # 15
      p = p[15:]
      length_bits_consumed += 15
      
      while subpacket_total_length_bits_consumed < sub_packet_length:
        (parsed_subpacket, subpacket_length_bits_consumed) = parse_packet(p)
        subpacket_total_length_bits_consumed += subpacket_length_bits_consumed
        p = p[subpacket_length_bits_consumed:]
        parsed_subpackets.append(parsed_subpacket)

    if I == 1:
      sub_packet_count = int(p[0:11], 2) # 11
      p = p[11:]
      length_bits_consumed += 11
      
      for i in range(sub_packet_count):
        (parsed_subpacket, subpacket_length_bits_consumed) = parse_packet(p)
        subpacket_total_length_bits_consumed += subpacket_length_bits_consumed
        p = p[subpacket_length_bits_consumed:]
        parsed_subpackets.append(parsed_subpacket)
      
    parsed_packet = [V,T,parsed_subpackets]
    length_bits_consumed += subpacket_total_length_bits_consumed
    return (parsed_packet, length_bits_consumed)
    
  else:
    print('ERROR')
    exit()
    
  
   
def version_sum(parsed_packet):
  [version, _, value] = parsed_packet
  if type(value) is list:
    version += sum(map(version_sum, value))
  return version

getit = {
  0 : lambda value : sum(map(evalp, value)),
  1 : lambda value : reduce(mul, map(evalp, value)),
  2 : lambda value : min(map(evalp, value)),
  3 : lambda value : max(map(evalp, value)),
  4 : lambda value : value,
  5 : lambda value : int( evalp(value[0]) >  evalp(value[1]) ),
  6 : lambda value : int( evalp(value[0]) <  evalp(value[1]) ),
  7 : lambda value : int( evalp(value[0]) == evalp(value[1]) ),
}

def evalp(parsed_packet):
  [_, packet_type, value] = parsed_packet
  return getit[packet_type](value)

def do_parse_packet(s):
  (parsed_packet, _) = parse_packet(s)
  return version_sum(parsed_packet), evalp(parsed_packet)

def hex_to_bin(s):
  return ''.join(map(lambda x : "{0:04b}".format(int(x,16)), s))

with open("input.txt", "r") as file:
  for line in file.readlines():
    line = hex_to_bin(line.rstrip('\n'))
    print(do_parse_packet(line))
