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
        
        