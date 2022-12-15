def find_first_k_different(k, char_list):
    for i in range(len(char_list)):
        if len(set(char_list[i:i+k])) == k:
            return i

x = open(0)
for line in x:
    print( find_first_k_different(  4, line.rstrip() ) +  4 )
    print( find_first_k_different( 14, line.rstrip() ) + 14 )
