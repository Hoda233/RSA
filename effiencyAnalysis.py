import rsa
import alphabet
import charConversion
import time
import matplotlib.pyplot as plt

effiency_file = open("effiency_test.txt", "r")
lines = effiency_file.read().splitlines()

enc_time=[]
dec_time=[]
key_sizes=[]

i =0
while i < len(lines)-1: 
    
    key_size=int(lines[i])
    key_sizes.append(key_size)

    public, private = rsa.generate_keypair(int(key_size))
    e,n=public

    message=lines[i+1]
    i+=2

    # process a message
    message=message.lower()
    message=alphabet.alphabet_encoding(message)
    message=charConversion.char_conversion_encoding(message)

    # calculate encryption time
    start = time.time()
    ciphertext=rsa.encrypt(message,public)
    end = time.time()
    enc_time.append(end-start)
    print('time to encrypt: ' ,end-start)

    # calculate decryption time
    start = time.time()
    decrypted=rsa.decrypt(int(ciphertext),private)
    end = time.time()
    dec_time.append(end-start)
    print('time to decrypt: ' ,end-start)

    decrypted=charConversion.char_conversion_decoding(decrypted)
    plaintext=alphabet.alphabet_decoding(decrypted)
    print('Message Received: ')
    print(plaintext)

# write results in a file
with open('effiency_results.txt', 'w') as f:
    for j in range(0,len(key_sizes)):
            f.write(str(key_sizes[j]) + ' ' +str(enc_time[j])+' ' +str(dec_time[j]))
            f.write('\n')
f.close()

# plot the results
fig, ax = plt.subplots()
ax.plot(key_sizes, enc_time)
ax.set_xlabel('Key size n (bits)')
ax.set_ylabel('Encryption time (seconds)')
ax.set_title('Effiency')
plt.show()