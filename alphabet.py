# Char ASCII space->32 0:9->48:57 a:z->97:122
# Mapping     space->36 0:9->0:9 a:z->10:35

# function to convert chars to its mapping
def alphabet_encoding(message):

    x=len(message)%5          #if (length mod 5)=0, the message are complete 
    if(x):
        for i in range(0,5-x):
            message+=' '
    
    new_message=[]

    for i in range(0,len(message)):
        # get char ascii 
        x=ord(message[i])
        if(ord(message[i])>=48 and ord(message[i])<=57):
            x-=48
        elif(ord(message[i])>=97 and ord(message[i])<=122):
            x-=87
        else:
            x=36
        new_message.append(x)

    return(new_message)

# function to return back chars from its mapping
def alphabet_decoding(message): 

    new_message=''

    for i in range(0,len(message)):
        if(message[i]>=10 and message[i]<=35):
            x=97+(message[i]-10)
        elif(message[i]>=0 and message[i]<=9):
            x=48+(message[i])
        else:
            x=32
        new_message+=chr(x)

    return(new_message)