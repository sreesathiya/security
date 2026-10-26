from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

# SENDER SIDE
message = input("Enter message: ")
password = input("Enter password: ")

# Generate AES key using SHA-1
key = hashlib.sha1(password.encode()).digest()[:16]

iv = get_random_bytes(16)

# Encrypt message
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(message.encode(), 16))

# Calculate SHA-1 hash of ciphertext
sender_hash = hashlib.sha1(ciphertext).hexdigest()

print("\n--- SENDER SIDE ---")
print("Ciphertext:", ciphertext.hex())
print("SHA-1 Hash:", sender_hash)

# TAMPERING SIMULATION
choice = input("\nSimulate tampering? (yes/no): ").lower()

received_ciphertext = bytearray(ciphertext)

if choice == "yes":
    received_ciphertext[0] ^= 1
    print("Tampering simulated!")

received_ciphertext = bytes(received_ciphertext)

# RECEIVER SIDE
print("\n--- RECEIVER SIDE ---")
print("Received Ciphertext:", received_ciphertext.hex())
print("Received Hash:", sender_hash)

# Calculate hash of received ciphertext
calculated_hash = hashlib.sha1(received_ciphertext).hexdigest()

print("Calculated Hash:", calculated_hash)

# Verify hash
if calculated_hash == sender_hash:
    print("\nHash Match! Ciphertext is unchanged.")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(
        cipher.decrypt(received_ciphertext), 16
    ).decode()

    print("Decrypted Message:", decrypted)

else:
    print("\nMODIFIED ERROR!")
    print("Ciphertext has been modified.")
    print("Decryption rejected.")
