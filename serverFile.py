import socket 
import rsa
import alphabet
import charConversion
import time

s = socket.socket() 
print ("Socket successfully created")

host=socket.gethostname()
port=7634
s.connect((host,port))

public, private = rsa.generate_keypair(1024)

msg=s.recv(1024).decode()
msg=str(msg)
msg=msg[1:-1] 
msg = msg.split(',') 
e=int(msg[0])
n=int(msg[1])
other_public=e,n

msg=str(public)
s.send(msg.encode())
time.sleep(0.01)

def send():
    print('Enter Message:')
    message = input(' -> ') 

    message=message.lower()
    message=alphabet.alphabet_encoding(message)

    for i in range(0,len(message),5):
        sub_message=message[i:i+5]
        
        sub_message=charConversion.char_conversion_encoding(sub_message)
    

        ciphertext=rsa.encrypt(sub_message,other_public)
        s.send(str(ciphertext).encode())
        time.sleep(0.01)
    
    
    end_msg='@'
    s.send(end_msg.encode())
    time.sleep(0.01)


def recieve():

    plaintext=''
    while True:
        ciphertext=s.recv(1024)

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

try:
    while True:
        send()
        recieve()
except KeyboardInterrupt:
    print('Close connection')
    s.close()
    

