import random
import string
from math import sqrt

def is_prime(a):       #Checking whether a number is prime or not
    if a < 2:
        return False
    for i in range(2, int(sqrt(a)) + 1):     
        if a % i == 0:
            return False
    return True

def gcd(a,b):      #GCD
    while a!=b:
        if a>b:
            a=a-b
        elif b>a:
            b=b-a
    return a

while True:       #Finds two distinct prime numbers p and q
    p = random.randint(100,1000)
    q = random.randint(100,1000)
    if is_prime(p) and is_prime(q) and p != q:
        break

n = p * q
phi = (p - 1) * (q - 1)

while True:       #Choose e so that gcd(e, φ(n)) = 1
    e = random.randint(2, phi - 1)
    if gcd(e, phi) == 1:
        break

d=pow(e, -1, phi)

a=[' '] +  list(string.digits) + list(string.ascii_uppercase) + list(string.ascii_lowercase)      #Characters
b=[32]
for i in range(48, 58):  
    b.append(i)
for i in range(65, 91):
    b.append(i)
for i in range(97, 123):
    b.append(i)

message = input("Enter a message: ")
m=list(message)

for i in range(len(m)):       #Converts each character in the message to ASCII code
    m[i]= b[a.index(m[i])]

ciphertext = []       #Encrypts every character of the message
for i in range(len(m)):
    ciphertext.append(pow(m[i], e, n))

print("Ciphertext:", ciphertext)
print("Public key (n, e):", (n, e))

desiphred_message = []       #Deciphers the encrypted message
for i in range(len(ciphertext)):
    desiphred_message.append(pow(ciphertext[i], d, n))

for i in range(len(desiphred_message)):
    desiphred_message[i] = a[b.index(desiphred_message[i])]

print("Decrypted message:", ''.join(desifred_message))
print("Private key (n, d):", (n, d))

