from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair (2048 bits)
key = RSA.generate(2048)

# Export keys
private_key = key.export_key()
public_key = key.publickey().export_key()

# Display generated keys
print("========== RSA KEY GENERATION ==========")
print("\nPublic Key:\n")
print(public_key.decode())

print("\nPrivate Key:\n")
print(private_key.decode())

# Accept plaintext from user
plaintext = input("\nEnter Plaintext: ")

# Create cipher object using public key
public_cipher = PKCS1_OAEP.new(RSA.import_key(public_key))

# Encrypt plaintext
ciphertext = public_cipher.encrypt(plaintext.encode())

# Display ciphertext in hexadecimal
print("\nEncrypted Ciphertext (Hexadecimal):")
print(binascii.hexlify(ciphertext).decode())

# Create cipher object using private key
private_cipher = PKCS1_OAEP.new(RSA.import_key(private_key))

# Decrypt ciphertext
decrypted_text = private_cipher.decrypt(ciphertext).decode()

# Display recovered plaintext
print("\nDecrypted Plaintext:")
print(decrypted_text)

# Verification
if plaintext == decrypted_text:
    print("\nVerification: SUCCESS")
    print("The decrypted plaintext matches the original plaintext.")
else:
    print("\nVerification: FAILED")
