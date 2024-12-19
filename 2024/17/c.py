#for x in range(8):
# for y in range(8):
#  for z in range(8):
#   for w in range(8):
#    for u in range(8):
#     for v in range(8):
#      for t in range(8):
#       a = x + y*8 + z*8**2 + w*8**3 + u*8**4 + v*8**5 + t*8**6
#       print(f'{a},{x},{y},{z},{w},{u},{v},{t} : ',end='')

def ff(a,i):

       output = []

       b = 0
       c = 0

       while a != 0 and len(output) < i:
    
        b = a % 8       # extract the lowest three bits of a
        b = b ^ 6       # flip the two high bits of b
        c = a // (2**b) # shift a right b bits
        b = b ^ c       # 
        b = b ^ 7       # flip the bits of b

        output.append(b % 8)

#        print(b % 8, end=',')    # print b as a three bit number
    
        a = a // (2**3) # shift a right 3 bits
    
#       print()
       return output

# >>> a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q = [2,2,6,5,2,1,3,2,7,5,3,1,1,7,2,1,0]
# >>> int(f'{q}{p}{o}{n}{m}{l}{k}{j}{i}{h}{g}{f}{e}{d}{c}{b}{a}',8)

for a in [2]:
 for b in [2]:
  for c in [6]:
   for d in [5]:
    for e in [2]:
     for f in [1]:
      for g in [3]:
       for h in [2,3]:
        for i in [3,7]:
         for j in [1,3,5,7]:
          for k in range(8):
           for l in range(8):
            for m in range(8):
             for n in range(8):
              for o in range(8):
               for p in range(8):
                for q in range(8):
                 print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,ff(int(f'{q}{p}{o}{n}{m}{l}{k}{j}{i}{h}{g}{f}{e}{d}{c}{b}{a}',8),16))
