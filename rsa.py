import random
import string
from math import sqrt

def is_prime(a):       #Sade olub olmamagi yoxluyur
    if a < 2:
        return False
    for i in range(2, int(sqrt(a)) + 1):     
        if a % i == 0:
            return False
    return True

def gcd(a,b):      #Ebob
    while a!=b:
        if a>b:
            a=a-b
        elif b>a:
            b=b-a
    return a

while True:       #2 dene birbirinnen ferqli p ve q sade ededleri tapir
    p = random.randint(100,1000)
    q = random.randint(100,1000)
    if is_prime(p) and is_prime(q) and p != q:
        break

n = p * q
phi = (p - 1) * (q - 1)

while True:       #phi ile ebob'u 1 olan e tapir
    e = random.randint(2, phi - 1)
    if gcd(e, phi) == 1:
        break

d=pow(e, -1, phi)

a=[' '] +  list(string.digits) + list(string.ascii_uppercase) + list(string.ascii_lowercase)      #karakterler
b=[32]
for i in range(48, 58):  
    b.append(i)
for i in range(65, 91):
    b.append(i)
for i in range(97, 123):
    b.append(i)

message = input("Enter a message: ")
m=list(message)

for i in range(len(m)):       #mesjdaki her karakteri ascii koduna cevirir
    m[i]= b[a.index(m[i])]

ciphertext = []       #mesajin her karakterini sifreleyir
for i in range(len(m)):
    ciphertext.append(pow(m[i], e, n))

print("Ciphertext:", ciphertext)
print("Public key (n, e):", (n, e))

desifred_message = []       #sifrelenmis mesaji desifreleyir
for i in range(len(ciphertext)):
    desifred_message.append(pow(ciphertext[i], d, n))

for i in range(len(desifred_message)):
    desifred_message[i] = a[b.index(desifred_message[i])]

print("Decrypted message:", ''.join(desifred_message))
print("Private key (n, d):", (n, d))
