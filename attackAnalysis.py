import rsa
import alphabet
import charConversion
import attack
import time
import matplotlib.pyplot as plt

attack_file = open("attack_test.txt", "r")
lines = attack_file.read().splitlines()

attack_time=[]
key_sizes=[]
n_keys=[]
d_keys=[]

i =0
while i < len(lines)-1: 
    
    key_size=int(lines[i])
    key_sizes.append(key_size)

    public, _ = rsa.generate_keypair(int(key_size))

    message=lines[i+1]
    i+=2

    # process a message to try to attack
    message=message.lower()
    message=alphabet.alphabet_encoding(message)
    message=charConversion.char_conversion_encoding(message)
    ciphertext=rsa.encrypt(message,public)

    # try to break and get the private key
    e,n=public
    start = time.time()
    d=attack.get_private_key(n,e)
    end = time.time()
    n_keys.append(n)
    d_keys.append(d)
    attack_time.append(end-start)
    print('time to get key ',end-start ,'key size: ',key_size)

    # check if attacking is successful
    is_attacked=attack.attack_check(ciphertext,message,n,d)
    if(is_attacked):
        print("Attacked","Private Key(d): ",d,' (n): ', n)
    else:
        print("Attack Failed")

# write results in a file
with open('attack_results.txt', 'w') as f:
    for j in range(0,len(key_sizes)):
        f.write(str(key_sizes[j]) + ' '+str(n_keys[j])+' '+str(d_keys[j])+' '+str(attack_time[j]))
        f.write('\n')
f.close()

# plot the results
fig, ax = plt.subplots()
ax.plot(key_sizes, attack_time)
ax.set_xlabel('Key size n (bits)')
ax.set_ylabel('Break time (seconds)')
ax.set_title('Attacking')
plt.show()
