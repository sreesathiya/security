
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

# AES key (16 bytes for AES-128)
key = b'1234567890123456'

# SENDER SIDE
message = input("Enter plaintext: ")

# Calculate SHA-1 hash of plaintext
sender_hash = hashlib.sha1(message.encode()).hexdigest()

print("\n--- SENDER SIDE ---")
print("Plaintext:", message)
print("SHA-1 Hash:", sender_hash)

# Encrypt plaintext using AES
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(message.encode(), 16))

print("Encrypted Ciphertext:", ciphertext.hex())

# RECEIVER SIDE
print("\n--- RECEIVER SIDE ---")

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(ciphertext), 16).decode()

print("Decrypted Plaintext:", decrypted)

# Calculate SHA-1 hash of decrypted plaintext
receiver_hash = hashlib.sha1(decrypted.encode()).hexdigest()

print("Receiver SHA-1 Hash:", receiver_hash)

# Compare hashes
if sender_hash == receiver_hash:
    print("HASH MATCHED")
    print("Message is unchanged.")
else:
    print("MESSAGE MODIFIED")
    print("Hash verification failed.")
