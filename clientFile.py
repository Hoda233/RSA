import socket 
import rsa
import alphabet
import charConversion
import time

s = socket.socket() 
print ("Socket successfully created")

host=socket.gethostname()
port=7634
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("connected with",addr)

public, private = rsa.generate_keypair(1024)


j=0
while j < 2:
    msg=str(public[j])
    c.send(msg.encode())
    j+=1

j=0
while j < 2:
    msg=c.recv(1024)
    if j == 0:
        e =int (msg)
    if j == 1:
        n = int(msg)   
    j+=1

other_public=(e,n)    

def send():
    print('Enter Message:')
    message = input(' -> ') 

    message=message.lower()
    message=alphabet.alphabet_encoding(message)

    for i in range(0,len(message),5):
        sub_message=message[i:i+5]

        sub_message=charConversion.char_conversion_encoding(sub_message)
        
        ciphertext=rsa.encrypt(sub_message,other_public)
        c.send(str(ciphertext).encode())
        time.sleep(0.1)
    
    
    end_msg='@'
    c.send(end_msg.encode())
    time.sleep(1)



def recieve():

    plaintext=''
    while True:
        ciphertext=c.recv(1024)

        if b'@' in ciphertext:
            print('end')
            break 
        ciphertext=int(ciphertext)
        decrypted=rsa.decrypt(ciphertext,private)
        decrypted=charConversion.char_conversion_decoding(decrypted)
        decrypted=alphabet.alphabet_decoding(decrypted)
        
        plaintext+=decrypted

    print('Message Received: ')
    print(plaintext)

while True:
    recieve()
    send()
