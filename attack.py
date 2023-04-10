import rsa

# function to factoerize n to get p,q then calculate d
def get_private_key(n,e):
    
    p=2
    while(p<=int((n**0.5)+1)):
        if n % p == 0:
            q = n//p
            break
        p+=1

    phi=(p-1)*(q-1)
    d = rsa.mod_inverse(e,phi)
    return (d)


# function to decrypt ciphertext using obtained private key 
# compare decrypted ciphertext and plaintext to check if attacking is done or not
def attack_check(C,P,n,d):

    atacked=False
    private_key = d, n 
    new_P=rsa.decrypt(C,private_key)

    if(P==new_P):
        atacked=True

    return (atacked,new_P)