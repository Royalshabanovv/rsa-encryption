import random
import sympy
from math import gcd

p = sympy.randprime(2**1023,2**1024)
q = sympy.randprime(2**1023,2**1024)

n = p * q
phi = (p - 1) * (q - 1)

while gcd(e := random.randint(2, phi-1), phi) != 1:
    pass

d=pow(e, -1, phi)

msg = input("Enter message: ")
cipher = [pow(ord(c), e, n) for c in msg]
print("Cipher:", ' '.join(map(str, cipher)))

plain = ''.join(chr(pow(c, d, n)) for c in cipher)
print("Decrypted:", ' '.join(map(str, plain)))

print("Public key (n, e):")
print("n =", n)
print("e =", e)

print("Private key (n, d):")
print("n =", n)
print("d =", d)