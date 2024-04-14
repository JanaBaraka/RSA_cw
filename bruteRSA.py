import time 
import random 
import math

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+ 2) == 0:
            return False
        i += 6
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num
        
def generate_keys(bits):
    #generate p and q
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    #e must be coprime to phi
    while gcd(e, phi) != 1:
        e+=1

    return (n, e), (p, q)

def brute_force_d(n, e, c):
    phi = (p - 1) * (q - 1)
    d = 1
    attempts = 0
    while True:
        attempts += 1
        if (d * e) % phi == 1:
            break
        d += 1
    return d, attempts

start_time = time.time()

public_key, private_key = generate_keys(8) # Change the bits value to 8 or 16 for cw requiements

end_time = time.time()
execution_time = end_time - start_time

n, e = public_key
p, q = private_key

print("Public Key: (n, e) ", public_key)
print("Private Key: (p, q) ", private_key)


#message to be encrypted
msg = 12
print("Message: ", msg)


#encrypt the message
c = pow(msg, e, n)
print("Encrypted Message: ", c)

start_time = time.time()

d, attempts = brute_force_d(n, e, c)

end_time = time.time()
execution_time += end_time - start_time


print("Brute Forced d, 'private exponent' is: ", d)
print("Attempts made: ", attempts)

#decrypt the message
m = pow(c, d, n)

print("Decrypted Message: ", m)
print("Execution Time: ", execution_time)

