from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

key = b'1234567890123456'

# SENDER SIDE
message = input("Enter plaintext: ")

# Encrypt plaintext using AES
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(message.encode(), 16))

# Compute SHA-1 hash of ciphertext
sender_cipher_hash = hashlib.sha1(ciphertext).hexdigest()

# Compute SHA-1 hash of plaintext
sender_plain_hash = hashlib.sha1(message.encode()).hexdigest()

print("\n--- SENDER SIDE ---")
print("Ciphertext:", ciphertext.hex())
print("Ciphertext SHA-1:", sender_cipher_hash)
print("Plaintext SHA-1:", sender_plain_hash)

# Optional tampering simulation
choice = input("\nSimulate ciphertext tampering? (yes/no): ").lower()

received_ciphertext = bytearray(ciphertext)

if choice == "yes":
    received_ciphertext[0] ^= 1
    print("Tampering simulated!")

received_ciphertext = bytes(received_ciphertext)

# RECEIVER SIDE
print("\n--- RECEIVER SIDE ---")

# Verify ciphertext hash before decryption
receiver_cipher_hash = hashlib.sha1(
    received_ciphertext
).hexdigest()

print("Received Ciphertext SHA-1:", receiver_cipher_hash)

if receiver_cipher_hash != sender_cipher_hash:
    print("MODIFIED ERROR: Ciphertext has changed!")
else:
    print("Ciphertext hash matched.")

    # Decrypt ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(
        cipher.decrypt(received_ciphertext), 16
    ).decode()

    print("Decrypted Plaintext:", decrypted)

    # Compute hash of decrypted plaintext
    receiver_plain_hash = hashlib.sha1(
        decrypted.encode()
    ).hexdigest()

    print("Receiver Plaintext SHA-1:", receiver_plain_hash)

    # Verify plaintext hash
    if receiver_plain_hash == sender_plain_hash:
        print("PLAINTEXT HASH MATCHED")
        print("Message verified successfully.")
    else:
        print("PLAINTEXT HASH MISMATCH")
        print("Message has been modified.")
