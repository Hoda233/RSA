# function to encode the mapping of char 
# by taking evey 5 integers [c4,c3,c2,c1,c0] and apply this formula summation(ci*(37^i))
def char_conversion_encoding(message):

    
    k=4
    sum=0
    for i in range(0,len(message)):
        sum+=message[i]*(37**(k))
        k-=1

    return sum

def char_conversion_decoding(number):
        
    temp_array=[]
    for i in range(0,5):
        temp_array.insert(0,int(number%37))
        number/=37
    return temp_array



# print(char_conversion_encoding([17,18,36,28,7]))
# print(char_conversion_decoding(char_conversion_encoding([17,18,36,28,7])))