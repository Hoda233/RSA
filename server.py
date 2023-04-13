import socket 
import rsa
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
        is_closed=chatFunctions.recieve(s,private)
        # print(is_closed)
        if(is_closed):
            break
        

except KeyboardInterrupt:
    print('Close connection')
    s.close()