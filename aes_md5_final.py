from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

# ---------- SENDER SIDE ----------

message = input("Sender - Enter message: ")
password = input("Enter secret password: ")

# Generate AES key using MD5
key = hashlib.md5(password.encode()).digest()

# Generate IV
iv = get_random_bytes(16)

# Encrypt message using AES
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(message.encode(), 16))

# Calculate MD5 hash of ciphertext
sender_hash = hashlib.md5(ciphertext).hexdigest()

print("\n--- SENDER SIDE ---")
print("Ciphertext:", ciphertext.hex())
print("MD5 Hash:", sender_hash)

# ---------- TAMPERING SIMULATION ----------

choice = input("\nSimulate tampering? (yes/no): ").lower()

received_ciphertext = bytearray(ciphertext)

if choice == "yes":
    received_ciphertext[0] ^= 1
    print("Tampering simulated!")

received_ciphertext = bytes(received_ciphertext)

# ---------- RECEIVER SIDE ----------

print("\n--- RECEIVER SIDE ---")

received_hash = sender_hash

print("Received Ciphertext:", received_ciphertext.hex())
print("Received Hash:", received_hash)

# Calculate hash of received ciphertext
calculated_hash = hashlib.md5(received_ciphertext).hexdigest()

print("Calculated Hash:", calculated_hash)

# Verify ciphertext integrity
if calculated_hash == received_hash:
    print("\nHash Match! Ciphertext is unchanged.")

    # Decrypt only if hash matches
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(
        cipher.decrypt(received_ciphertext), 16
    ).decode()

    print("Decrypted Message:", decrypted)

else:
    print("\nMODIFIED ERROR!")
    print("Ciphertext has been modified.")
    print("Decryption rejected.")
