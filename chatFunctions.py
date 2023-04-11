import rsa
import alphabet
import charConversion
import time

def receive_publickey(socket):
    msg=socket.recv(1024).decode()
    msg=str(msg)
    msg=msg[1:-1] 
    msg = msg.split(',') 
    e=int(msg[0])
    n=int(msg[1])
    other_public=e,n
    return other_public

def send_publickey(socket,msg):
    msg=str(msg)
    socket.send(msg.encode())
    time.sleep(0.01)

def send(socket,other_public):

    print('Enter Message:')
    message = input(' -> ') 

    message=message.lower()
    message=alphabet.alphabet_encoding(message)

    for i in range(0,len(message),5):
        sub_message=message[i:i+5]
        sub_message=charConversion.char_conversion_encoding(sub_message)
    
        ciphertext=rsa.encrypt(sub_message,other_public)
        socket.send(str(ciphertext).encode())
        time.sleep(0.01)
    
    
    end_msg='@'
    socket.send(end_msg.encode())
    time.sleep(0.01)

def recieve(socket,private):

    plaintext=''
    while True:
        ciphertext=socket.recv(1024)

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

