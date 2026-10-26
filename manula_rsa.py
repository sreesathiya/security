# RSA Algorithm using User-Defined Functions

import math

# Function to check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to find GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Input two prime numbers
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

if p == q or not is_prime(p) or not is_prime(q):
    print("Enter two different prime numbers!")
    exit()

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Choose public exponent e
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

# Calculate private exponent d
d = mod_inverse(e, phi)

print("\nPublic Key:", (e, n))
print("Private Key:", (d, n))

# Input plaintext as an integer
message = int(input("\nEnter message as an integer: "))

if message < 0 or message >= n:
    print("Message must be between 0 and", n - 1)
    exit()

# Encryption
ciphertext = pow(message, e, n)
print("Encrypted Message:", ciphertext)

# Decryption
decrypted = pow(ciphertext, d, n)
print("Decrypted Message:", decrypted)

# Verification
if message == decrypted:
    print("Verification: SUCCESS")
else:
    print("Verification: FAILED")