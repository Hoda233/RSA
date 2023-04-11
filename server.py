import socket 
import rsa
import alphabet
import charConversion
import time
import chatFunctions

s = socket.socket() 
print ("Socket successfully created")

host=socket.gethostname()
port=7634
s.connect((host,port))

public, private = rsa.generate_keypair(1024)

other_public=chatFunctions.receive_publickey(s)
chatFunctions.send_publickey(s,public)

try:
    while True:
        chatFunctions.send(s,other_public)
        chatFunctions.recieve(s,private)
        

except KeyboardInterrupt:
    print('Close connection')
    s.close()