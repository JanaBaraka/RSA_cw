import math
import random
import time

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def generate_keys(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 2
    while math.gcd(e, phi) != 1:
        e += 1
    
    return (n, e), (p, q)

def factorize(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors


# Generating keys
start_time = time.time()

public_key, private_key = generate_keys(16)  # Change the bits value to 8 or 16 for coursework requirements

end_time = time.time()
execution_time = end_time - start_time

n, e = public_key
p, q = private_key

print("Public Key (n, e):", public_key)
print("Private Key (p, q):", private_key)

# Message to be encrypted
msg = 12
print("Message data =", msg)

# Encryption c = (msg ^ e) % n
c = pow(msg, e, n)
print("Encrypted data =", c)

# Factorizing N to obtain p and q
start_time = time.time()

factors = factorize(n)
p = factors[0]
q = factors[1]

end_time = time.time()
execution_time += end_time - start_time

print("Factored p and q:", (p, q))

# Calculate private exponent d using Extended Euclidean Algorithm
phi = (p - 1) * (q - 1)
d = modular_inverse(e, phi)
print("Private Exponent d =", d)

# Decryption m = (c ^ d) % n
m = pow(c, d, n)
print("Original Message Sent =", m)

print("Execution time:", execution_time, "seconds")
