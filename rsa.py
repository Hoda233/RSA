import sympy

# get GCD of 2 numbers using theorem of gcd(a,b)=gcd(b, a % b), gcd(x,0)=x
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# get to use in mod inverse to get inverse of a mod b
def extended_gcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

# get inverse of a mod m
def mod_inverse(a, m):
    g, x,y = extended_gcd(a, m)
    if g != 1:
        return None  
    else:
        return x % m

# generate prime numbers with spesific no of bits
def generate_prime(bitlength):
    a = '1'+'0'*(bitlength-1)
    b = '1'*bitlength
    p = sympy.randprime(int(a, 2), int(b, 2))
    return p

# generate private&public keys
def generate_keypair(keysize):
    m=0
    if(keysize%2!=0): #if n odd 
        m=1

    p = generate_prime(int(keysize/2)+m)
    q = generate_prime(int(keysize/2))
    n = p * q
    phi = (p-1)*(q-1)
    e = sympy.randprime(1,phi)
    d = mod_inverse(e,phi)
    if e != d:
        return ((e, n), (d, n))  


# encrypt by publickey -> C=M^e mod n
def encrypt(plaintext, publickey):
    e, n = publickey
    if plaintext > n:
        print('Message is too large for key')
    ciphertext = pow(plaintext, e, n)
    return ciphertext 

# decrypt by privatekey -> M=C^d mod n
def decrypt(ciphertext, privatekey):
    d, n = privatekey
    plaintext = pow(ciphertext, d, n)
    return plaintext 