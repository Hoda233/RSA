# function to encode the mapping of char 
# by taking evey 5 integers [c4,c3,c2,c1,c0] 
# apply this formula summation(ci*(37^i))
def char_conversion_encoding(message):

    k=4
    sum=0
    for i in range(0,len(message)):
        sum+=message[i]*(37**(k))
        k-=1

    return sum

# 17 · 37^4 + 18 · 37^3 + 36 · 37^2 + 28 · 37^1 + 7 = 32,822,818
# (17 · 37^4 + 18 · 37^3 + 36 · 37^2 + 28 · 37^1 + 7) %37=7
# (17 · 37^4 + 18 · 37^3 + 36 · 37^2 + 28 · 37^1 + 7)/37
# 17 · 37^3 + 18 · 37^2 + 36 · 37^1 + 28  + 0......

def char_conversion_decoding(number):
        
    temp_array=[]
    for i in range(0,5):
        temp_array.insert(0,int(number%37))
        number/=37
    return temp_array