import socket 
import rsa
import chatFunctions

s = socket.socket() 
print ("Socket successfully created")

host=socket.gethostname()
port=7634
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("connected with",addr)

public, private = rsa.generate_keypair(1024)

chatFunctions.send_publickey(c,public)
other_public=chatFunctions.receive_publickey(c)

try:
    while True:
        chatFunctions.recieve(c,private)
        chatFunctions.send(c,other_public)

except KeyboardInterrupt:
    print('Close connection')
    s.close()
    c.close()