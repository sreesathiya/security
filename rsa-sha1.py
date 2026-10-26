import hashlib

# Given values
p = 23
g = 5
a = 6
b = 15

# Calculate public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Alice's public key A =", A)
print("Bob's public key B =", B)

# Calculate shared secrets independently
alice_secret = pow(B, a, p)
bob_secret = pow(A, b, p)

print("Alice's shared secret =", alice_secret)
print("Bob's shared secret =", bob_secret)

# Check whether secrets match
if alice_secret == bob_secret:
    print("Shared secrets match")
else:
    print("Shared secrets do not match")

# Derive session key using SHA-1
digest = hashlib.sha1(str(alice_secret).encode()).hexdigest()
session_key = digest[:8]

print("SHA-1 digest =", digest)
print("Session key =", session_key)

# Information visible to an eavesdropper
print("\nEve can see:")
print("p =", p)
print("g =", g)
print("A =", A)
print("B =", B)

print("Eve cannot easily calculate the shared secret")
# In real systems, secure parameter sizes are essential.