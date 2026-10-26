import hashlib
import math

p = 47
q = 59
e = 17

message = "PAY RAHUL RS 5000"
tampered_message = "PAY RAHUL RS 9000"

# Calculate RSA values
n = p * q
phi = (p - 1) * (q - 1)

if math.gcd(e, phi) != 1:
    print("Invalid public exponent")
    exit()

d = pow(e, -1, phi)

print("n =", n)
print("phi(n) =", phi)
print("Public key:", (e, n))
print("Private key:", (d, n))


# Calculate MD5 digest and reduced hash
def calculate_hash(text):
    digest = hashlib.md5(text.encode()).hexdigest()
    H = int(digest, 16) % n
    return digest, H


digest, H = calculate_hash(message)

print("\nMessage:", message)
print("MD5 digest:", digest)
print("Reduced hash H =", H)


# Sign using private key
S = pow(H, d, n)
print("Digital signature S =", S)


# Verify using public key
H_verify = pow(S, e, n)
print("Verified hash H' =", H_verify)

if H_verify == H:
    print("Signature is VALID")
else:
    print("Signature is INVALID")


# Test message tampering
new_digest, new_H = calculate_hash(tampered_message)

print("\nTampered message:", tampered_message)
print("New MD5 digest:", new_digest)
print("New reduced hash =", new_H)

if pow(S, e, n) == new_H:
    print("Tampered message: Signature VALID")
else:
    print("Tampered message: Signature INVALID")